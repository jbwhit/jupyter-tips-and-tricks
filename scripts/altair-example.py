#!/usr/bin/env python
"""
Altair Tooltip Example
======================

An example script that demonstrates how JupyterLab can create interactive altair plots.
"""
import sys

import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(x='petalLength', y='petalWidth', color='species')


cars = data.cars()

LITERS_PER_GALLON = 3.78541

cars['Miles_per_Liter'] = cars['Miles_per_Gallon'] * LITERS_PER_GALLON

alt.Chart(cars).mark_circle(size=60).encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).interactive()