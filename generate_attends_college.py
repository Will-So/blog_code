from blog_code.constants import HOME_DIR

def generate_non_correlated_values():
    population = int(2e6)

    school_rating = np.random.normal(2, 2, population)
    parents_income = np.random.normal(40, 40, population) + 20
    additional_factors = np.random.normal(-0, 20, population)
    gpa = (np.random.normal(3, 0.5, population)).clip(0, 4.2)
    has_car = has_car = np.random.rand(population) > .6

    parents_income[parents_income < 0] = 0

    attends_college = 1 / (1 + np.exp(-parameters))
    attends_college = attends_college > .5

    b0, b1, b2, b3, b4 = -25, 1.5, 0.05, 4, 1
    parameters = b0 + b1 * school_rating + b2 * parents_income + b3 * gpa + b4 * additional_factors

    attends_college = 1 / (1 + np.exp(-parameters))

    df = pd.DataFrame({'attends_college': attends_college.astype(int), 'gpa': gpa, 'parents_income': parents_income,
                       'school_rating': school_rating, })

    df.to_parquet()