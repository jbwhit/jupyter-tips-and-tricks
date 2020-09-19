# -*- coding: utf-8 -*-
"""
Examples
"""
import argparse
import sys
import logging
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context('poster', font_scale=1.3)

from insight import __version__

__author__ = "jbwhit"
__copyright__ = "jbwhit"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def plot_prod_vs_hours(
    df, color_index=0, output_file="../img/production-vs-hours-worked.png"
):
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.regplot(
        df["Labor_Hours"],
        df["Production_short_tons"],
        ax=ax,
        color=sns.color_palette()[color_index],
    )
    ax.set_xlabel("Labor Hours Worked")
    ax.set_ylabel("Total Amt Produced")
    x = ax.set_xlim(-9_506_023.0, 204_993_853.0)
    y = ax.set_ylim(-51_476_801.0, 746_280_580.0)
    fig.tight_layout()
    fig.savefig(output_file)

