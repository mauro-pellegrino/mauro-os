# -*- coding: utf-8 -*-
"""Helpers for the labelled-frame ASCII style (box-drawing, inset section headers)."""
W = 92  # inner width

def _rule(label, left, right):
    lab = " " + label + " " if label else ""
    return left + "─" + lab + "─" * (W - 1 - len(lab)) + right

def top(label=""):  return _rule(label, "┌", "┐")
def sect(label=""): return _rule(label, "├", "┤")
def bot():          return "└" + "─" * W + "┘"
def line(text=""):  return "│" + (" " + text).ljust(W) + "│"
def kv(k, v, kw=16, ind=3):
    return line(" " * (ind - 1) + k.ljust(kw) + v)

def inner(label, rows, ind=18, iw=46):
    """A nested labelled box, indented."""
    pad = " " * ind
    lab = " " + label + " "
    out = [line(pad + "┌─" + lab + "─" * (iw - 2 - len(lab)) + "┐")]
    for r in rows:
        out.append(line(pad + "│ " + r.ljust(iw - 2) + "│"))
    out.append(line(pad + "└" + "─" * iw + "┘"))
    return out

def sign(handle="@maurojpelle"):
    return line(handle.rjust(W - 2))
