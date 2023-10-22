from nlgeval import compute_metrics



metrics_dict = compute_metrics(hypothesis='sml-one.csv',
                                references=['nl.csv'],no_skipthoughts=True, no_glove=True)
