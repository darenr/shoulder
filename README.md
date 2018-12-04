# shoulder

A library to find the point in a series where the fitted curve tangent reaches a threshold angle.

In many situations there's a drop off curve where it's useful to know the value for which the fitted curve tangent reaches a threshold. For example, in looking at feature importances in machine learning the feature weights might look like the below.

![example curve](https://raw.githubusercontent.com/darenr/shoulder/master/assets/ex-curve.png)

This library takes a series of values either as an array or numpy array, a tangent angle, a direction (descending to tangent angle or ascending to tangent angle) and returns the value which corresponds to that angle.
