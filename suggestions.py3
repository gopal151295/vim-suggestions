import sched, time
import random
import os
s = sched.scheduler(time.time, time.sleep)
suggestions = [
    '1. CM: H - move to top of screen',
    '2. CM: M - move to middle of screen',
    '3. CM: L - move to bottom of screen',
    '4. CM: W - jump forwards to the start of a word (words can contain punctuation)',
    '5. CM: E - jump forwards to the end of a word (words can contain punctuation)',
    '6. CM: B - jump backwards to the start of a word (words can contain punctuation)',
    '7. CM: % - move to matching character (default supported pairs: "()", "{}", "[]" - use :h matchpairs in vim for more info)',
    '8. CM: } - jump to next paragraph (or function/block, when editing code)',
    '9. CM: { - jump to previous paragraph (or function/block, when editing code)',
    '10. CM: Ctrl + b - move back one full screen',
    '11. CM: Ctrl + f - move forward one full screen',
    '12. CM: Ctrl + d - move forward 1/2 a screen',
    '13. CM: Ctrl + u - move back 1/2 a screen',
    '14. Ed: J - join line below to the current one with one space in between',
    '15. Ed: gJ - join line below to the current one without space in between',
    '16. Ed: cc - change (replace) entire line',
    '17. Ed: s - delete character and substitute text',
    '18. Ed: S - delete line and substitute text (same as cc)',
    '19. V: V - start linewise visual mode',
    '20. V: o - move to other end of marked area',
    '21. V: Ctrl + v - start visual block mode',
    '22. V: O - move to other corner of block',
    '23. V: aw - mark a word',
    '24. V: ab - a block with ()',
    '25. V: aB - a block with {}',
    '26. V: ib - inner block with ()',
    '27. V: iB - inner block with {}',
    '28. V: iB - inner block with {}',
    '29. V: iB - INNER block with {}',
    '30. V: iB - inner block with {}',
    '31. VM: ~ - switch case',
    '32. CM: C	change to end of line',
    '33. CM: D	delete to end of line',
    '34. CM: (	jumps to the previous sentence',
    '35. CM: )	jumps to the next sentence',
    '36. CM: [[	jumps to the previous section',
    '37. CM: ]]	jumps to the next section',
    '38. CM: []	jump to the end of the previous section',
    '39. CM: ][	jump to the end of the next section',
    '40. Ed: gI	Insert text in column 1 times.',
    '41. CM: z.	Center the screen on the cursor',
    '42. CM: zt	Scroll the screen so the cursor is at the top',
    '43. CM: zb	Scroll the screen so the cursor is at the bottom',
    '44. CM: Ctrl + e - scroll one line up',
    '45. CM: Ctrl + y - scroll one line down',
    '46. CM: * - search forward for word under cursor',
    '47. CM: # - search backwards for word under cursor',
    '48. CM: n next match in same direction',
    '49. CM: N next match in opposite direction',
    '50. CM: N next match in opposite direction',
    '51. CM: / search forward',
    '52. CM: 0 jumps directly to the beginning of the line(hard)',
    '53. CM: ^ jumps to first non blank character',
    '54. CM: $ jumps to end of line',
    '55. CM: fx - jump to next `x` character,
    '56. CM: Fx jumps to previous `x` character',
    '57. CM: tx jumps forward to right before `x` character',
    '58. CM: Tx jumps backwards to right before `x` character',
]
c = 0
t = 60 # 60 sec
def getSuggestion():
    global suggestions
    i = random.randint(0, len(suggestions) - 1)
    # print(i)
    msgToDisplay = suggestions[i]
    return msgToDisplay
def do_something(sc):
    msg = getSuggestion()
    command = 'notify-send "' + msg + '"'
    os.system(command)
    global c
    c += 1
    print ("Printed %d suggestions.." %(c))
    
    s.enter(t, 1, do_something, (sc,))

s.enter(t, 1, do_something, (s,))
s.run()
