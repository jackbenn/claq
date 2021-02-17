# CLAQ

## Command-Line Analysis and Query Tools for data

This is (to be) a set of command-line tools for manipulating and transforming data. For the most part, the tools take in data from a file or STDIN as a tab-separated table of numbers, without at header, and returns the data in the same format.

## Tools

Final names and tools TBD

Probably these are sub commands on a single command.

* cut - select or manipulate columns
* sort - reorder rows
* aggr - group by and aggregate
* narrow - switch the data from wide to narrow format (a.k.a., stack, melt, normalize
* widen - switch the data from  narrow to wide format (a.k.a., unstack, pivot, denormalize)
* where - select rows
* format - outputs as human-readable text table, markdown, markup, etc.
* parse - parse into table from various formats
* plot - generate a plot of the data
* ...

## Format

The general format each command expects and outputs is tab-separated numbers without a header.

This can be altered in a couple ways. First, certain options will allow all commands to read (or output?) code in a slightly different format (e.g., with a header, CSV).

Second, special characters will provide additional information, such they are unlikely to show up unexpectedly, e.g., header and types. In particular, if the first character is `!`, the first row (excluding the leading `!`) is treated as a header row.