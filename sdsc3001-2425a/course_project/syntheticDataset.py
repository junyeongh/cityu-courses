import random


def generate_balanced_synthetic_stream(n, jaccard_true):
    # Calculate sizes
    similarity_coefficient = (2 * jaccard_true) / (1 + jaccard_true)
    intersection_size = int(n * similarity_coefficient)
    unique_elements = n - intersection_size

    stream = []

    # Add intersection elements
    for i in range(intersection_size):
        stream.append(["setA", i])
        stream.append(["setB", i])

    # Add unique elements for set A
    for i in range(intersection_size, intersection_size + unique_elements):
        stream.append(["setA", i])

    # Add unique elements for set B
    for i in range(intersection_size + unique_elements, intersection_size + 2 * unique_elements):
        stream.append(["setB", i])

    # Shuffle the stream to avoid bias
    random.shuffle(stream)

    return stream


def generate_unbalanced_synthetic_stream(n, jaccard_true):
    # Calculate size of set B
    set_b_size = int(n * jaccard_true)

    stream = []

    # Add all elements for set A
    for i in range(n):
        stream.append(["setA", i])

    # Add elements for set B (selected from set A)
    for i in range(set_b_size):
        stream.append(["setB", i])

    # Shuffle the stream to avoid bias
    random.shuffle(stream)

    return stream


if __name__ == "__main__":
    import polars as pl
    import numpy as np
    import sys
    import os

    # print(os.getcwd() in sys.path)
    sys.path.append(os.getcwd())
    # print(os.getcwd() in sys.path)

    from hashSketch import MinHash, B_bitMinHash, OddSketch, MaxLogHash  # noqa:E402

    def compare_all_methods(stream, num_runs, k=128, n=10000):
        """
        Compare all similarity estimation methods over multiple runs

        Args:
            stream: list of tuples representing the stream
            num_runs: number of runs with different random seeds
            k: number of hash functions
            n: number of elements in the stream (cardinality)

        Returns:
            dict: Dictionary containing error statistics for each method
        """
        # Initialize lists to store results for each method
        results = {"minhash": [], "bbit": [], "oddsketch": [], "maxlog": []}

        for run in range(num_runs):
            print("Run:", run + 1)
            # Set random seed for this run
            random.seed(run)

            # Regular MinHash estimation
            minhash = MinHash(k, random_seed=run)
            minhash.process_stream(stream)
            results["minhash"].append(minhash.estimate_similarity())

            # b-bit MinHash estimation
            b = 4  # b-bit MinHash parameter
            bbit_minhash = B_bitMinHash(k, b, random_seed=run)
            bbit_minhash.process_stream(stream)
            results["bbit"].append(bbit_minhash.estimate_similarity())

            # Odd Sketch estimation
            z = 4 * k  # Odd Sketch size
            odd_sketch = OddSketch(k, z, random_seed=run)
            odd_sketch.process_stream(stream)
            results["oddsketch"].append(odd_sketch.estimate_similarity())

            # MaxLogHash estimation
            maxlog = MaxLogHash(k, random_seed=run)
            maxlog.process_stream(stream)
            results["maxlog"].append(maxlog.estimate_similarity())

        print("Results:", results)
        return results

    # Parameters
    k = 128  # Number of hash functions
    n = 10_000  # cardinality of the sets
    runs = 10

    # Initialize empty lists for each statistic
    balanced_jaccard_values = []
    balanced_mean_results = []
    balanced_median_results = []
    balanced_std_results = []
    balanced_rmse_results = []
    balanced_bias_results = []

    # Balanced stream
    for i in np.arange(0.80, 1.00, 0.02):
        print("Synthetic balanced stream with Jaccard similarity:", i)
        # Generate synthetic stream
        stream = generate_balanced_synthetic_stream(n, i)
        results = compare_all_methods(stream, runs)

        stats = {}
        for method, estimates in results.items():
            errors = np.array(estimates) - i
            stats[method] = {
                "mean": np.mean(estimates),
                "median": np.median(estimates),
                "std": np.std(estimates),
                "rmse": np.sqrt(np.mean(errors**2)),
                "bias": np.mean(errors),
            }

        # Append values for each statistic
        balanced_jaccard_values.append(i)
        balanced_mean_results.append(
            {
                "jaccard": i,
                "minhash": stats["minhash"]["mean"],
                "bbit": stats["bbit"]["mean"],
                "oddsketch": stats["oddsketch"]["mean"],
                "maxlog": stats["maxlog"]["mean"],
            }
        )
        balanced_median_results.append(
            {
                "jaccard": i,
                "minhash": stats["minhash"]["median"],
                "bbit": stats["bbit"]["median"],
                "oddsketch": stats["oddsketch"]["median"],
                "maxlog": stats["maxlog"]["median"],
            }
        )
        balanced_std_results.append(
            {
                "jaccard": i,
                "minhash": stats["minhash"]["std"],
                "bbit": stats["bbit"]["std"],
                "oddsketch": stats["oddsketch"]["std"],
                "maxlog": stats["maxlog"]["std"],
            }
        )
        balanced_rmse_results.append(
            {
                "jaccard": i,
                "minhash": stats["minhash"]["rmse"],
                "bbit": stats["bbit"]["rmse"],
                "oddsketch": stats["oddsketch"]["rmse"],
                "maxlog": stats["maxlog"]["rmse"],
            }
        )
        balanced_bias_results.append(
            {
                "jaccard": i,
                "minhash": stats["minhash"]["bias"],
                "bbit": stats["bbit"]["bias"],
                "oddsketch": stats["oddsketch"]["bias"],
                "maxlog": stats["maxlog"]["bias"],
            }
        )

    # Create DataFrames
    df_balance_mean = pl.DataFrame(balanced_mean_results)
    df_balance_median = pl.DataFrame(balanced_median_results)
    df_balance_std = pl.DataFrame(balanced_std_results)
    df_balance_rmse = pl.DataFrame(balanced_rmse_results)
    df_balance_bias = pl.DataFrame(balanced_bias_results)

    df_balance_mean.write_parquet("balanced_mean_results.parquet")
    df_balance_median.write_parquet("balanced_median_results.parquet")
    df_balance_std.write_parquet("balanced_std_results.parquet")
    df_balance_rmse.write_parquet("balanced_rmse_results.parquet")
    df_balance_bias.write_parquet("balanced_bias_results.parquet")

    # Initialize empty lists for each statistic
    unbalanced_jaccard_values = []
    unbalanced_mean_results = []
    unbalanced_median_results = []
    unbalanced_std_results = []
    unbalanced_rmse_results = []
    unbalanced_bias_results = []

    # Unbalanced stream
    for i in np.arange(0.80, 1.00, 0.02):
        print("Synthetic unbalanced stream with Jaccard similarity:", i)
        # Generate synthetic stream
        stream = generate_unbalanced_synthetic_stream(n, i)
        results = compare_all_methods(stream, runs)

        stats = {}
        for method, estimates in results.items():
            errors = np.array(estimates) - i
            stats[method] = {
                "mean": np.mean(estimates),
                "median": np.median(estimates),
                "std": np.std(estimates),
                "rmse": np.sqrt(np.mean(errors**2)),
                "bias": np.mean(errors),
            }

        # Append values for each statistic
        unbalanced_jaccard_values.append(i)
        unbalanced_mean_results.append(
            {
                "jaccard": i,
                "minhash": stats["minhash"]["mean"],
                "bbit": stats["bbit"]["mean"],
                "oddsketch": stats["oddsketch"]["mean"],
                "maxlog": stats["maxlog"]["mean"],
            }
        )
        unbalanced_median_results.append(
            {
                "jaccard": i,
                "minhash": stats["minhash"]["median"],
                "bbit": stats["bbit"]["median"],
                "oddsketch": stats["oddsketch"]["median"],
                "maxlog": stats["maxlog"]["median"],
            }
        )
        unbalanced_std_results.append(
            {
                "jaccard": i,
                "minhash": stats["minhash"]["std"],
                "bbit": stats["bbit"]["std"],
                "oddsketch": stats["oddsketch"]["std"],
                "maxlog": stats["maxlog"]["std"],
            }
        )
        unbalanced_rmse_results.append(
            {
                "jaccard": i,
                "minhash": stats["minhash"]["rmse"],
                "bbit": stats["bbit"]["rmse"],
                "oddsketch": stats["oddsketch"]["rmse"],
                "maxlog": stats["maxlog"]["rmse"],
            }
        )
        unbalanced_bias_results.append(
            {
                "jaccard": i,
                "minhash": stats["minhash"]["bias"],
                "bbit": stats["bbit"]["bias"],
                "oddsketch": stats["oddsketch"]["bias"],
                "maxlog": stats["maxlog"]["bias"],
            }
        )

    # Create DataFrames
    df_unbalance_mean = pl.DataFrame(unbalanced_mean_results)
    df_unbalance_median = pl.DataFrame(unbalanced_median_results)
    df_unbalance_std = pl.DataFrame(unbalanced_std_results)
    df_unbalance_rmse = pl.DataFrame(unbalanced_rmse_results)
    df_unbalance_bias = pl.DataFrame(unbalanced_bias_results)

    df_unbalance_mean.write_parquet("unbalance_mean_results.parquest")
    df_unbalance_median.write_parquet("unbalance_median_results.parquest")
    df_unbalance_std.write_parquet("unbalance_std_results.parquest")
    df_unbalance_rmse.write_parquet("unbalance_rmse_results.parquest")
    df_unbalance_bias.write_parquet("unbalance_bias_results.parquest")
