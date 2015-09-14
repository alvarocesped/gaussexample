#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, pars):
    A, sigma, mu = pars
    return A * np.exp(-(x - mu)**2 / 2 / sigma**2)

A = 1.
sigma = 1.
mu = 0.
pars = A, sigma, mu

x_full = np.linspace(-4, 4, 100)
y_full = gaussian(x_full, pars)

x_sigma1 = np.linspace(-1, 1, 100)
y_sigma1 = gaussian(x_sigma1, pars)

x_sigma2 = np.linspace(-2, 2, 100)
y_sigma2 = gaussian(x_sigma2, pars)

x_sigma3 = np.linspace(-3, 3, 100)
y_sigma3 = gaussian(x_sigma3, pars)



xticks = (-3., -2., -1., 0., 1., 2., 3.)
xtick_labels = (r"$\mu - 3 \sigma$",
                r"$\mu - 2 \sigma$",
                r"$\mu - \sigma$",
                r"$\mu$",
                r"$\mu + \sigma$",
                r"$\mu + 2 \sigma$",
                r"$\mu + 3 \sigma$")

fig = plt.figure(1, figsize=(6, 4))
ax = fig.add_subplot(111)

ax.axhline(0, color='b')



ax.fill_between(x_full, y_full, edgecolor='b', facecolor='#00FFFF')
ax.fill_between(x_sigma3, y_sigma3, y2=0, edgecolor='', facecolor='#0066FF')
ax.fill_between(x_sigma2, y_sigma2, y2=0, edgecolor='', facecolor='#0033FF')
ax.fill_between(x_sigma1, y_sigma1, y2=0, edgecolor='', facecolor='#0000FF')

ax.set_xticks(xticks)
ax.set_xticklabels(xtick_labels, rotation=90)
ax.set_yticks([])

ax.set_xlim(-4, 4)
ax.set_ylim(-0.1, 1.1)

ax.text(0, 0.4, '68%', fontsize=14, color='w', va='center', ha='center')

fig.subplots_adjust(bottom=0.20)

ax.tick_params(axis='x', which='major', labelsize=13, top='off')

plt.text(0.9,0.9,'Alvaro Cesped\nalvaro_cesped@live.cl',fontsize=11)

plt.savefig('gauss.png')
