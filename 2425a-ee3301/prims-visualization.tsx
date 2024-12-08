import React, { useState, useEffect } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Play, RotateCcw } from 'lucide-react';

const PrimsVisualization = () => {
  // Graph data
  const initialGraph = {
    nodes: [
      { id: 'A', x: 100, y: 100 },
      { id: 'B', x: 250, y: 50 },
      { id: 'C', x: 400, y: 100 },
      { id: 'D', x: 100, y: 250 },
      { id: 'E', x: 250, y: 300 },
      { id: 'F', x: 400, y: 250 }
    ],
    edges: [
      { from: 'A', to: 'B', weight: 4 },
      { from: 'A', to: 'D', weight: 3 },
      { from: 'B', to: 'C', weight: 5 },
      { from: 'B', to: 'D', weight: 6 },
      { from: 'B', to: 'E', weight: 8 },
      { from: 'C', to: 'E', weight: 4 },
      { from: 'C', to: 'F', weight: 2 },
      { from: 'D', to: 'E', weight: 5 },
      { from: 'E', to: 'F', weight: 7 }
    ]
  };

  const [currentStep, setCurrentStep] = useState(0);
  const [visitedNodes, setVisitedNodes] = useState(new Set(['A']));
  const [mstEdges, setMstEdges] = useState([]);
  const [currentEdge, setCurrentEdge] = useState(null);
  const [algorithmSteps, setAlgorithmSteps] = useState([]);
  const [isPlaying, setIsPlaying] = useState(false);

  // Initialize algorithm steps
  useEffect(() => {
    const steps = calculatePrimSteps();
    setAlgorithmSteps(steps);
  }, []);

  const calculatePrimSteps = () => {
    const steps = [];
    const visited = new Set(['A']);
    const mst = [];

    while (visited.size < initialGraph.nodes.length) {
      let minEdge = null;
      let minWeight = Infinity;

      // Find the minimum weight edge connecting a visited node to an unvisited node
      for (const edge of initialGraph.edges) {
        const isFromVisited = visited.has(edge.from);
        const isToVisited = visited.has(edge.to);

        if ((isFromVisited && !isToVisited) || (!isFromVisited && isToVisited)) {
          if (edge.weight < minWeight) {
            minWeight = edge.weight;
            minEdge = edge;
          }
        }
      }

      if (minEdge) {
        const newNode = visited.has(minEdge.from) ? minEdge.to : minEdge.from;
        steps.push({
          edge: minEdge,
          newNode,
          mstEdges: [...mst]
        });
        visited.add(newNode);
        mst.push(minEdge);
      }
    }

    return steps;
  };

  const nextStep = () => {
    if (currentStep < algorithmSteps.length) {
      const step = algorithmSteps[currentStep];
      setCurrentEdge(step.edge);
      setVisitedNodes(prev => new Set([...prev, step.newNode]));
      setMstEdges(step.mstEdges);
      setCurrentStep(prev => prev + 1);
    } else {
      setIsPlaying(false);
    }
  };

  const reset = () => {
    setCurrentStep(0);
    setVisitedNodes(new Set(['A']));
    setMstEdges([]);
    setCurrentEdge(null);
    setIsPlaying(false);
  };

  useEffect(() => {
    let timer;
    if (isPlaying) {
      timer = setTimeout(nextStep, 1000);
    }
    return () => clearTimeout(timer);
  }, [isPlaying, currentStep]);

  return (
    <Card className="w-full max-w-4xl">
      <CardHeader>
        <CardTitle>Prim's Algorithm Visualization</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="flex flex-col items-center space-y-4">
          <svg className="w-full h-96 bg-white rounded-lg" viewBox="0 0 500 350">
            {/* Draw edges */}
            {initialGraph.edges.map((edge, idx) => {
              const from = initialGraph.nodes.find(n => n.id === edge.from);
              const to = initialGraph.nodes.find(n => n.id === edge.to);
              const isMST = mstEdges.some(e => 
                (e.from === edge.from && e.to === edge.to) ||
                (e.from === edge.to && e.to === edge.from)
              );
              const isCurrentEdge = currentEdge && 
                ((currentEdge.from === edge.from && currentEdge.to === edge.to) ||
                 (currentEdge.from === edge.to && currentEdge.to === edge.from));

              return (
                <g key={`edge-${idx}`}>
                  <line
                    x1={from.x}
                    y1={from.y}
                    x2={to.x}
                    y2={to.y}
                    stroke={isCurrentEdge ? '#f59e0b' : isMST ? '#10b981' : '#e5e7eb'}
                    strokeWidth={isMST || isCurrentEdge ? 3 : 2}
                  />
                  <text
                    x={(from.x + to.x) / 2}
                    y={(from.y + to.y) / 2}
                    dy={-10}
                    textAnchor="middle"
                    fill="#6b7280"
                    className="text-sm"
                  >
                    {edge.weight}
                  </text>
                </g>
              );
            })}

            {/* Draw nodes */}
            {initialGraph.nodes.map((node, idx) => (
              <g key={`node-${idx}`}>
                <circle
                  cx={node.x}
                  cy={node.y}
                  r={20}
                  fill={visitedNodes.has(node.id) ? '#10b981' : '#white'}
                  stroke={visitedNodes.has(node.id) ? '#059669' : '#e5e7eb'}
                  strokeWidth="2"
                />
                <text
                  x={node.x}
                  y={node.y}
                  dy="6"
                  textAnchor="middle"
                  fill={visitedNodes.has(node.id) ? 'white' : '#374151'}
                  className="text-sm font-medium"
                >
                  {node.id}
                </text>
              </g>
            ))}
          </svg>

          <div className="flex space-x-4">
            <Button
              onClick={() => setIsPlaying(!isPlaying)}
              disabled={currentStep >= algorithmSteps.length}
              className="flex items-center space-x-2"
            >
              <Play className="w-4 h-4" />
              <span>{isPlaying ? 'Pause' : 'Play'}</span>
            </Button>
            <Button
              onClick={reset}
              variant="outline"
              className="flex items-center space-x-2"
            >
              <RotateCcw className="w-4 h-4" />
              <span>Reset</span>
            </Button>
          </div>

          <div className="text-sm text-gray-600">
            {currentStep === 0 ? (
              "Starting from node A"
            ) : currentStep >= algorithmSteps.length ? (
              "Minimum Spanning Tree completed!"
            ) : (
              `Added edge ${currentEdge?.from}-${currentEdge?.to} with weight ${currentEdge?.weight}`
            )}
          </div>
        </div>
      </CardContent>
    </Card>
  );
};

export default PrimsVisualization;