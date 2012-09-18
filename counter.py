# coding=utf-8
import sublime, sublime_plugin

class CounterCommand(sublime_plugin.TextCommand):
    """
    • Sublime Text Counter •

    Inserts an incrementing counter at each cursor location.
    Optionally specify the starting value, incrementing value, and padding.

    [start]+/-[increment]:[padding]

    Input   Output
    -----   ------
    1       1, 2, 3, ...
    1+2     1, 3, 5, ...
    10      10, 11, 12, ...
    100-5   100, 95, 90, ...
    1:3     001, 002, 003, ...
    1+2:3   001, 003, 005, ...
    """
    def run(self, edit):
        self.begin_get_parameters()

    def begin_get_parameters(self):
        self.view.window().show_input_panel("Insert counter starting at", "1", self.end_get_parameters, None, None)

    def end_get_parameters(self, text):
        try:
            starting_value, incrementing, padding = self.parse_parameters(text)

            self.execute(starting_value, incrementing_value, padding)
        except:
            self.display_help()

    def parse_parameters(self, text):
        padding = 0
        if ':' in text:
            splits = text.split(':')
            padding = int(splits[1])
            text = splits[0]

        incrementing_value = 1
        if '+' in text:
            splits = text.split('+')
            incrementing_value = int(splits[1])
            text = splits[0]
        elif '-' in text:
            splits = text.split('-')
            incrementing_value = -int(splits[1])
            text = splits[0]

        starting_value = int(text)

        return starting_value, incrementing_value, padding

    def execute(self, starting_value, incrementing_value, padding):
        i = starting_value

        edit = self.view.begin_edit("counter")

        try:
            for region in self.view.sel():
                counter = ("%%0%dd" % padding) % i
                if region.begin() == region.end():
                    self.view.insert(edit, region.begin(), counter)
                else:
                    self.view.replace(edit, region, counter)

                i += incrementing_value
        finally:
            self.view.end_edit(edit)

    def display_help(self):
        sublime.status_message("Invalid counter parameters - see console for help.")
        print self.__class__.__doc__
