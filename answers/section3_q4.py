"""
α, the learning rate
lower bound of [0], which means that there is always some learning
upper bound of [1], which means that the maximum it can learn is the value of the reward itself.

β, the softmax temperature
lower bound of [0], so that the bias is always in favour of the option with the higher value
upper bound of [15], which is fairly liberal and would make for quite deterministic choices (you can simulate this!).

""";
