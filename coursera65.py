text = "X-DSPAM-Confidence:    0.8475"
textpos = text.find(':')
piece = text[textpos+1:]
end = float(piece)
print(end)