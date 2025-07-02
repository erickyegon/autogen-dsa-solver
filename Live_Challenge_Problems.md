# 🔥 LIVE CHALLENGE PROBLEMS FOR YOUTUBE RECORDING
## Copy-Paste Ready for Screen Sharing

---

## 🎯 CHALLENGE 1: DYNAMIC PROGRAMMING FACTORY OPTIMIZATION
**Timing: 17:00 - 21:00**
**Language: Python | Complexity: Expert | Focus: DP + Constraints**

### 📋 Problem Statement (Copy-Paste Ready):
```
I'm operating a mini-factory with a limited budget and energy supply. I have a list of N different machines. Each machine i has:

cost[i]: The monetary cost to acquire it.
energy_consumption[i]: The continuous energy it draws (e.g., kW/hour).
production_rate[i]: The units of product it produces per hour.
maintenance_interval[i]: The number of hours after which it requires a fixed 2-hour downtime for maintenance.

I have a total budget and a maximum total_energy_limit for all machines running concurrently. My goal is to select a subset of machines to acquire and operate for a fixed operational period of T hours such that:

1. The total acquisition cost does not exceed budget.
2. The aggregate energy consumption of all selected running machines at any given moment does not exceed total_energy_limit.
3. The total cumulative production over the T hours is maximized.

The maintenance downtime is critical: a machine i that runs from hour h to h + maintenance_interval[i] must then stop for two hours, starting from h + maintenance_interval[i], before it can resume. Multiple maintenance windows can overlap, and if a machine needs maintenance, its energy consumption drops to zero during that period, but obviously, its production also stops.

Provide a Python solution that identifies the optimal set of machines and the maximum production. Explain the underlying algorithm, its time complexity, and discuss how to handle the dynamic maintenance schedules efficiently.
```

### 🎯 Expected AI Solution Components:
- Dynamic programming with state space modeling
- Constraint satisfaction for budget/energy limits
- Maintenance window scheduling algorithm
- Time complexity: O(T × 2^N × E)
- Comprehensive test cases with edge cases

---

## 🎯 CHALLENGE 2: GRAPH-BASED FRAUD DETECTION
**Timing: 21:00 - 25:00**
**Language: Python | Complexity: Hard | Focus: Graph Algorithms + ML**

### 📋 Problem Statement (Copy-Paste Ready):
```
I have a large dataset representing financial transactions. Each transaction has: sender_account_id, receiver_account_id, amount, and timestamp. My objective is to build a system in Python that can detect unusual or potentially fraudulent transaction patterns.

Here's what I want it to do:

1. Construct a dynamic graph: Represent accounts as nodes and transactions as directed edges. The graph should be able to evolve as new transactions arrive (simulatable as adding new edges over time). Edges could be weighted by amount.

2. Identify Anomalies: I need to find 'anomalous' accounts or transaction sequences. Indicators of anomalies could include:
   - Unusual Degree Centrality: An account suddenly sending/receiving transactions from many disparate new accounts.
   - Abnormal Path Lengths/Cycles: Transactions forming unusually short or long paths, or quick, suspicious cycles (e.g., money sent out and immediately returned through multiple intermediaries).
   - Volume Spikes: An account's total transaction volume (in/out) spiking dramatically compared to its historical patterns.
   - Sub-Graph Analysis: Detecting highly interconnected small groups of accounts with high transaction frequencies that are otherwise isolated from the main network.

3. Provide an anomaly score: For each account or transaction, output a score or flag indicating its likelihood of being anomalous, along with a brief explanation of why it's considered anomalous (e.g., "high new recipient count," "short cycle detected").

The solution should leverage appropriate Python graph libraries (like networkx) and discuss real-time processing considerations versus batch processing.
```

### 🎯 Expected AI Solution Components:
- NetworkX dynamic graph construction
- Centrality analysis (degree, betweenness, closeness)
- Cycle detection algorithms
- Statistical anomaly scoring
- Real-time vs batch processing discussion

---

## 🎯 CHALLENGE 3: REINFORCEMENT LEARNING NETWORK ROUTING
**Timing: 29:00 - 32:00 (Bonus Challenge)**
**Language: Python | Complexity: Expert | Focus: RL + Dynamic Graphs**

### 📋 Problem Statement (Copy-Paste Ready):
```
Imagine a simplified computer network represented as a graph where nodes are routers and edges are links with varying latencies (weights). These latencies can change dynamically over time (e.g., due to congestion).

I need a Python solution that uses Reinforcement Learning (RL) to find the most efficient path for packets between any given source and destination router. The goal for the RL agent is to minimize the cumulative latency experienced by packets.

Here's the setup:

1. Network Representation: A graph (e.g., adjacency list/matrix) of N routers.

2. Dynamic Latency: Simulate latency changes on edges. For instance, every 10 simulation steps, randomly update a few edge latencies within a given range.

3. RL Agent:
   - The state for the agent should be the current router and the destination router.
   - The actions are choosing the next router to send the packet to.
   - The reward should be based on the negative latency of moving from the current router to the chosen next router.

4. Learning Process: The agent should learn an optimal policy over many simulated packet transmissions.

5. Evaluation: After training, demonstrate the agent's learned path for a few sample (source, destination) pairs and compare its cumulative latency to what a standard shortest path algorithm (like Dijkstra's or Bellman-Ford) would find on a static snapshot of the network (to show the benefit of dynamic learning).

The AI should primarily focus on implementing a suitable RL algorithm (e.g., Q-learning or SARSA), setting up the environment, and demonstrating the learning process. Discussion on hyperparameter tuning and scalability would be a bonus.
```

### 🎯 Expected AI Solution Components:
- Q-learning or SARSA implementation
- Dynamic network environment simulation
- State-action space modeling
- Training loop with exploration/exploitation
- Performance comparison with Dijkstra's algorithm

---

## 🎯 R CHALLENGE 1: ADVANCED DATA CLEANING & TIME SERIES
**Timing: 25:00 - 29:00**
**Language: R | Complexity: Medium | Focus: Data Science + Statistics**

### 📋 Problem Statement (Copy-Paste Ready):
```
I have a messy dataset in R, potentially loaded from a CSV, that represents sensor readings over time. The data consists of three columns: timestamp (POSIXct format), sensor_id (character string), and value (numeric). The issues are:

1. Missing Data: Many value entries are NA, but they aren't randomly missing. Sometimes, an entire sensor_id will have NAs for a consecutive period.

2. Irregular Intervals: The timestamp values are not perfectly regular (e.g., some readings might be every 5 minutes, others every 7, and some might be missing entirely).

3. Outliers: There are some extreme, isolated value outliers that are clearly erroneous.

My goal is to first clean and prepare this data, which involves:
- Ensuring timestamp is correctly parsed.
- Filling in missing value data using a suitable imputation method (e.g., linear interpolation for short gaps, but a more sophisticated approach like na_kalman from imputeTS for longer gaps, applied per sensor_id).
- Identifying and replacing outliers. A simple approach might be z-score based, but I'm open to more robust methods.

Finally, after cleaning, I need to resample the data so that each sensor_id has readings at a consistent, regular interval (e.g., every 10 minutes), aggregating values if necessary (e.g., using the mean for a specified window). I'd also like a visualization of the original noisy data for one sensor, and then a plot showing the imputed and resampled data for the same sensor to demonstrate the cleanup.
```

### 🎯 Expected AI Solution Components:
- POSIXct timestamp parsing and handling
- imputeTS package for sophisticated imputation
- Statistical outlier detection and replacement
- Data resampling with regular intervals
- ggplot2 before/after visualization

---

## 🎯 R CHALLENGE 2: MIXED-EFFECTS MODELING (BACKUP)
**Language: R | Complexity: Hard | Focus: Statistical Modeling**

### 📋 Problem Statement (Copy-Paste Ready):
```
I have experimental data from an R data frame with three main columns: SubjectID (factor), TrialNum (integer), and ResponseTime (numeric). Each subject performed multiple trials. I suspect that response times vary both across subjects and within subjects over different trials.

My task is to perform a statistical analysis in R. Specifically, I want to:

1. Build a mixed-effects linear regression model where ResponseTime is the dependent variable. TrialNum should be a fixed effect, and I expect random intercepts for SubjectID. It's possible TrialNum also has a random slope by SubjectID, so I'd like the AI to consider that complexity if appropriate.

2. Interpret the model results, explaining the fixed effects, the random effects, and what they tell me about the data.

3. Visualize the data and model fit. I'd like a ggplot2 visualization that shows the ResponseTime for each SubjectID over TrialNum, with separate lines for each subject. Crucially, the plot should also display the overall fixed-effect trend from the model, and ideally, the individual fitted lines for each subject based on their random effects.
```

---

## 📝 RECORDING TIPS FOR CHALLENGES

### 🎬 Before Each Challenge:
1. **Set up screen sharing** with Streamlit app visible
2. **Copy problem statement** from this document
3. **Select appropriate language and complexity**
4. **Start screen recording** for backup

### 🎯 During Challenge Demonstration:
1. **Read problem aloud** while pasting into interface
2. **Highlight key complexity points** ("This combines DP with constraints...")
3. **Show AI collaboration in real-time** ("Watch the agents work together...")
4. **Explain solution approach** as AI generates code
5. **Highlight impressive aspects** ("This would take hours manually...")

### 🔥 If Challenge Fails:
1. **Stay calm and explain** what went wrong
2. **Show backup solution** if available
3. **Use as teaching moment** about AI limitations
4. **Move to next challenge** quickly

### ⚡ Time Management:
- **Challenge 1:** 4 minutes max
- **Challenge 2:** 4 minutes max  
- **R Challenge:** 4 minutes max
- **Bonus RL:** 3 minutes max
- **Keep buffer time** for explanations and wrap-up

### 🎤 Key Phrases to Use:
- **"This is happening in real-time, no editing"**
- **"Watch our AI team collaborate"**
- **"This is PhD-level complexity"**
- **"Notice how it adapts to [language] strengths"**
- **"The AI just solved in minutes what takes experts hours"**
