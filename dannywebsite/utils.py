def settings_to_use(args):
    """Helper function to determine which settings configuration to use."""

    test_settings = 'dannywebsite.settings_test'
    default_settings = 'dannywebsite.settings'

    return test_settings if 'test' in args else default_settings