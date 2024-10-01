import printing_functions as pf

# Now we use the code from printing_models.
unprinted_designs = ["castle", "polyhedral dice", "controller"]
printed_models = []

# Print the models while they print and the completed models.
pf.print_models(unprinted_designs, printed_models)
pf.show_completed(printed_models)
