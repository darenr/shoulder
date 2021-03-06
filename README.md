# shoulder

A library to find the point in a series where the fitted curve slope angle reaches a threshold.

In many situations there's a drop off curve where it's useful to know the value for which the fitted curve slope reaches a threshold. For example, in looking at feature importances in machine learning the feature weights might look like the below.

![example curve](https://github.com/darenr/shoulder/raw/master/assets/ex-curve.png)

This library takes a series of values either as an array or numpy array, a slope angle, a direction (descending to slope angle or ascending to slope angle) and returns the value which corresponds to that angle.
