import math
import mmh3
import numpy as np
import random

random_seed = 42
random.seed(random_seed)
# Parameters
k = 128  # Number of hash functions
n = 10_000  # cardinality of the sets


class MinHash:
    def __init__(self, k, random_seed=random_seed):
        """
        Initialize MinHash
        k: number of hash functions
        random_seed: random seed for reproducibility
        """
        self.k = k
        self.seed = random_seed
        self.totalShingles = (1 << 32) - 1
        self.minHashSignatures = {}  # Store signatures for each set
        self.randomNoA = self._hash_parameter()
        self.randomNoB = self._hash_parameter()

    def _hash_parameter(self):
        """Generate random hash parameters"""
        randList = []
        k_temp = self.k
        randIndex = random.randint(0, self.totalShingles - 1)
        randList.append(randIndex)
        while k_temp > 0:
            while randIndex in randList:
                randIndex = random.randint(0, self.totalShingles - 1)
            randList.append(randIndex)
            k_temp -= 1
        return randList

    def process_stream(self, stream):
        """
        Process streaming data
        stream: list of [set_id, element] pairs
        """
        for item in stream:
            set_id, element = item[0], item[1]

            # Initialize signature if not exists
            if set_id not in self.minHashSignatures:
                self.minHashSignatures[set_id] = [float("inf")] * self.k

            # Update minimum hash values
            for i in range(self.k):
                hash_value = (
                    self.randomNoA[i] * mmh3.hash(str(element), self.seed) + self.randomNoB[i]
                ) % self.totalShingles
                self.minHashSignatures[set_id][i] = min(self.minHashSignatures[set_id][i], hash_value)

    def estimate_similarity(self, setA="setA", setB="setB"):
        """
        Estimate Jaccard similarity between two sets
        setA, setB: identifiers of the sets to compare
        """
        if setA not in self.minHashSignatures or setB not in self.minHashSignatures:
            raise ValueError("Sets not found in signatures")

        # Count matching signatures
        matches = sum(1 for i in range(self.k) if self.minHashSignatures[setA][i] == self.minHashSignatures[setB][i])

        # Estimate Jaccard similarity
        return matches / self.k


class B_bitMinHash:
    def __init__(self, k, b, random_seed=random_seed):
        """
        Initialize b-bit MinHash
        k: number of hash functions
        b: number of bits to keep from each hash value
        random_seed: random seed for reproducibility
        """
        self.k = k
        self.b = b
        self.seed = random_seed
        self.totalShingles = (1 << 32) - 1
        self.minHashSignatures = {}  # Store original MinHash signatures
        self.bbitSignatures = {}  # Store b-bit signatures
        self.randomNoA = self._hash_parameter()
        self.randomNoB = self._hash_parameter()
        self.mask = (1 << b) - 1  # Mask for getting lowest b bits

    def _hash_parameter(self):
        """Generate random hash parameters"""
        randList = []
        k_temp = self.k
        randIndex = random.randint(0, self.totalShingles - 1)
        randList.append(randIndex)
        while k_temp > 0:
            while randIndex in randList:
                randIndex = random.randint(0, self.totalShingles - 1)
            randList.append(randIndex)
            k_temp -= 1
        return randList

    def _get_lowest_b_bits(self, value):
        """Extract lowest b bits from a value"""
        return value & self.mask

    def process_stream(self, stream):
        """
        Process streaming data
        stream: list of [set_id, element] pairs
        """
        # First compute regular MinHash signatures
        for item in stream:
            set_id, element = item[0], item[1]

            # Initialize signature if not exists
            if set_id not in self.minHashSignatures:
                self.minHashSignatures[set_id] = [float("inf")] * self.k

            # Update minimum hash values
            for i in range(self.k):
                hash_value = (
                    self.randomNoA[i] * mmh3.hash(str(element), self.seed) + self.randomNoB[i]
                ) % self.totalShingles
                self.minHashSignatures[set_id][i] = min(self.minHashSignatures[set_id][i], hash_value)

        # Convert MinHash signatures to b-bit signatures
        for set_id in self.minHashSignatures:
            self.bbitSignatures[set_id] = [
                self._get_lowest_b_bits(int(value)) for value in self.minHashSignatures[set_id]
            ]

    def estimate_similarity(self, setA="setA", setB="setB"):
        """
        Estimate Jaccard similarity between two sets using b-bit MinHash
        setA, setB: identifiers of the sets to compare
        """
        if setA not in self.bbitSignatures or setB not in self.bbitSignatures:
            raise ValueError("Sets not found in signatures")

        # Count matching b-bit signatures
        matches = sum(1 for i in range(self.k) if self.bbitSignatures[setA][i] == self.bbitSignatures[setB][i])

        # Estimate Jaccard similarity using b-bit MinHash formula
        # Formula: (matches/k - 1/2^b)/(1 - 1/2^b)
        denominator = 1.0 - 1.0 / (1 << self.b)
        numerator = matches / float(self.k) - 1.0 / (1 << self.b)

        return numerator / denominator


class OddSketch:
    def __init__(self, k, z, random_seed=random_seed):
        """
        Initialize Odd Sketch
        k: number of hash functions (for MinHash)
        z: number of bits in Odd Sketch
        random_seed: random seed for reproducibility
        """
        self.k = k
        self.z = z
        self.seed = random_seed
        self.totalShingles = (1 << 32) - 1
        self.minHashSignatures = {}  # Store MinHash signatures
        self.oddSketches = {}  # Store Odd Sketches
        self.randomNoA = self._hash_parameter()
        self.randomNoB = self._hash_parameter()

    def _hash_parameter(self):
        """Generate random hash parameters"""
        randList = []
        k_temp = self.k
        randIndex = random.randint(0, self.totalShingles - 1)
        randList.append(randIndex)
        while k_temp > 0:
            while randIndex in randList:
                randIndex = random.randint(0, self.totalShingles - 1)
            randList.append(randIndex)
            k_temp -= 1
        return randList

    def _compute_odd_sketch(self, minhash_signature):
        """
        Compute Odd Sketch from MinHash signature
        Uses XOR-based sketching
        """
        odd_sketch = np.zeros(self.z, dtype=bool)

        for i in range(self.k):
            # Hash (i, minhash_value) to position in odd sketch
            position = mmh3.hash(str((i, minhash_signature[i])), self.seed) % self.z
            odd_sketch[position] ^= True  # XOR operation

        return odd_sketch

    def process_stream(self, stream):
        """
        Process streaming data
        stream: list of [set_id, element] pairs
        """
        # First compute regular MinHash signatures
        for item in stream:
            set_id, element = item[0], item[1]

            # Initialize signature if not exists
            if set_id not in self.minHashSignatures:
                self.minHashSignatures[set_id] = [float("inf")] * self.k

            # Update minimum hash values
            for i in range(self.k):
                hash_value = (
                    self.randomNoA[i] * mmh3.hash(str(element), self.seed) + self.randomNoB[i]
                ) % self.totalShingles
                self.minHashSignatures[set_id][i] = min(self.minHashSignatures[set_id][i], hash_value)

        # Convert MinHash signatures to Odd Sketches
        for set_id in self.minHashSignatures:
            self.oddSketches[set_id] = self._compute_odd_sketch(self.minHashSignatures[set_id])

    def estimate_similarity(self, setA="setA", setB="setB"):
        """
        Estimate Jaccard similarity between two sets using Odd Sketch
        setA, setB: identifiers of the sets to compare
        """
        if setA not in self.oddSketches or setB not in self.oddSketches:
            raise ValueError("Sets not found in sketches")

        # Count differing bits between odd sketches
        hamming_distance = np.sum(self.oddSketches[setA] != self.oddSketches[setB])

        # Estimate Jaccard similarity using Odd Sketch formula
        # J = 1 + (z/4k)ln(1 - 2d/z)
        # where d is the Hamming distance and z is the sketch size
        if hamming_distance == self.z:
            return 0.0

        similarity = 1.0 + (self.z / (4.0 * self.k)) * np.log(1.0 - (2.0 * hamming_distance) / self.z)

        # Clamp similarity to [0,1]
        return max(0.0, min(1.0, similarity))


class MaxLogHash:
    def __init__(self, k, random_seed=random_seed):
        self.k = k
        self.seed = random_seed
        self.totalShingles = (1 << 32) - 1
        self.maxShingleID = {}
        self.randomNoA = self._hash_parameter()
        self.randomNoB = self._hash_parameter()

    def _hash_parameter(self):
        randList = []
        k_temp = self.k
        randIndex = random.randint(0, self.totalShingles - 1)
        randList.append(randIndex)
        while k_temp > 0:
            while randIndex in randList:
                randIndex = random.randint(0, self.totalShingles - 1)
            randList.append(randIndex)
            k_temp -= 1
        return randList

    def process_stream(self, stream):
        for item in stream:
            if item[0] in self.maxShingleID:
                max_hash_val_list = self.maxShingleID[item[0]][0]
                max_hash_sig_list = self.maxShingleID[item[0]][1]

                for x in range(self.k):
                    temp = (
                        self.randomNoA[x] * mmh3.hash(str(item[1]), self.seed) + self.randomNoB[x]
                    ) % self.totalShingles
                    temp = temp / float(self.totalShingles)
                    log_temp = -math.log(temp, 2)
                    hash_val = math.ceil(log_temp)

                    if hash_val > max_hash_val_list[x]:
                        max_hash_val_list[x] = hash_val
                        max_hash_sig_list[x] = 1
                    elif hash_val == max_hash_val_list[x]:
                        max_hash_sig_list[x] = 0

                self.maxShingleID[item[0]][0] = max_hash_val_list
                self.maxShingleID[item[0]][1] = max_hash_sig_list
            else:
                max_hash_val_list = [-1] * self.k
                max_hash_sig_list = [0] * self.k
                self.maxShingleID[item[0]] = [max_hash_val_list, max_hash_sig_list]

    def estimate_similarity(self, setA="setA", setB="setB"):
        con = 0
        for x in range(self.k):
            if self.maxShingleID[setA][0][x] > self.maxShingleID[setB][0][x] and self.maxShingleID[setA][1][x] == 1:
                con += 1
            elif self.maxShingleID[setA][0][x] < self.maxShingleID[setB][0][x] and self.maxShingleID[setB][1][x] == 1:
                con += 1

        jaccard_sim = 1.0 - con * (1 / float(self.k)) * (1 / 0.7213)
        return jaccard_sim
