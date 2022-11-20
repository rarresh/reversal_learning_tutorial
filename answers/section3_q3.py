"""
α

If you have a fast learning rate, you can adapt very quickly after a reversal,
but in the middle of a block, you change the value too readily when the 'unexpected' side is rewarded (you can see this clearly on the single-subject plots)
If you have a slow learning rate, your values change very slowly but you are a lot more stable in the middle of the block.
This is better for the 'low volatility' than for the 'high volatility' environment.

β
When beta is large, the choice probability strongly follows the value difference
When beta is small, the choice probability stays around 0.5 regardless of the value difference
This also means that the choices themselves are more random and so you learn a lot more about the not-so-good option.
""";
