import json
from core.flags import FlagType


class count(FlagType):
    @staticmethod
    def execute(type, threshold, operator, value):
        """
        Compares the value of of an input using ==, >, <, >=, or <=. See data/functions.json for argument information

        Returns:
            The result of the comparison
        """
        if not type or type == "json":
            var = len(json.loads(value))
        else:
            try:
                var = int(value)
            except ValueError:
                var = len(value)

        if operator == "g":
            if var > threshold:
                return True

        elif operator == "ge":
            if var >= threshold:
                return True

        elif operator == "l":
            if var < threshold:
                return True

        elif operator == "le":
            if var <= threshold:
                return True

        elif operator == "e":
            if var == threshold:
                return True
        else:
            if var == threshold:
                return True

        return False