#!/usr/bin/env python
"""
Altair Tooltip Example
======================

An example script that Jonathan lightly modified to make it work in a Notebook.
"""
import sys

import altair as alt

alt.renderers.enable("notebook")

from vega_datasets import data

iris = data.iris()
# alt.renderers.enable('default')

alt.Chart(iris).mark_point().encode(x="petalLength", y="petalWidth", color="species")


cars = data.cars()

LITERS_PER_GALLON = 3.78541

cars["Miles_per_Liter"] = cars["Miles_per_Gallon"] * LITERS_PER_GALLON

alt.Chart(cars).mark_circle(size=60).encode(
    x="Horsepower",
    y="Miles_per_Gallon",
    color="Origin",
    tooltip=["Name", "Origin", "Horsepower", "Miles_per_Gallon"],
).interactive()
