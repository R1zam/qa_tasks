class ParamsCreator:
    @staticmethod
    def create_param(param_name, param_value):
        return [param_name, param_value]

    @staticmethod
    def create_params(*args):
        return {k: v for k, v in args}