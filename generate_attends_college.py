"""
USEAGE

python generate_attends_college.py correlated
python generate_attends_college.py uncorrelated
"""
from blog_code.constants import BLOG_CODE_DIR
from os.path import join
import numpy as np
import pandas as pd

import click


@click.group()
def cli():
    pass


@click.command(name='uncorrelated')
def generate_non_correlated_values():
    population = int(2e6)

    school_rating = np.random.normal(2, 2, population)
    parents_income = np.random.normal(40, 40, population) + 20
    additional_factors = np.random.normal(-0, 20, population)
    gpa = (np.random.normal(3, 0.5, population)).clip(0, 4.2)
    has_car = np.random.rand(population) > .6

    parents_income[parents_income < 0] = 0

    b0, b1, b2, b3, b4 = -25, 1.5, 0.05, 4, 1
    parameters = b0 + b1 * school_rating + b2 * parents_income + b3 * gpa + b4 * additional_factors

    attends_college = 1 / (1 + np.exp(-parameters))
    attends_college = attends_college > .5

    df = pd.DataFrame({'attends_college': attends_college.astype(int), 'gpa': gpa, 'parents_income': parents_income,
                       'school_rating': school_rating, 'has_car': has_car})

    df.to_parquet(join(BLOG_CODE_DIR, 'data', 'uncorrelated_education.parquet'))


@click.command(name='correlated')
def generate_correlated_values():
    """"""
    population = int(2e6)
    family_background = np.random.normal(10, 20, population)
    school_rating = 0.96 * family_background * 2 + np.random.normal(0, 2, population)
    parents_income = .96 * family_background + np.random.normal(0, 1, population) + 20
    additional_factors = np.random.normal(-25, 10, population)
    gpa = (np.random.normal(3, 0.5, population) + .001 * parents_income).clip(0, 4.2)
    has_car = has_car = np.random.rand(population) > .6

    parents_income[parents_income < 0] = 0

    parameters = 2 * gpa + 1 * school_rating + 0.025 * parents_income + additional_factors - 2

    attends_college = 1 / (1 + np.exp(-parameters))
    attends_college = attends_college > .5

    df = pd.DataFrame({'attends_college': attends_college.astype(int), 'gpa': gpa, 'parents_income': parents_income,
                       'school_rating': school_rating, 'has_car': has_car.astype(int)})

    df.to_parquet(join(BLOG_CODE_DIR, 'data', 'correlated_education.parquet'))


cli.add_command(generate_correlated_values)
cli.add_command(generate_non_correlated_values)

if __name__ == '__main__':
    cli()
