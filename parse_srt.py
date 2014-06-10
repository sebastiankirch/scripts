import click
import pysrt

# parse an .srt subtitle file and optionally store the text and time information in a new text file
# 
# @author skirch
#
# options
#   -v / --overlap  [OPTIONAL, default=True] if the text in the srt file is overlapping or not
#   -o / --output   [OPTIONAL] output text file
#
# arguments
#   [1] .srt file to be processed
# 
@click.command()
@click.option('-v','--overlap', default=False, help='if the text in the srt file is overlapping', type=click.BOOL)
@click.option('-o','--output', default=False, help='output file')
@click.argument('file')
def parseSrt(file, overlap, output):
    subs = pysrt.open(file)
    entries = len(subs)

    fullText = subs[0].text.replace('\n', ' ')
    timeArray = ''

    if overlap:
        subs.shift(seconds=-3)

    time = getTimeInMilliseconds(subs[0].start)
    end = getTimeInMilliseconds(subs[0].end)
    difference = end - time

    text = subs[0].text.replace('\n', ' ')
    textArray = text.split(' ')

    if overlap:
        for x in xrange(0,len(textArray)):
            time += (difference / len(textArray))
            timeArray += str(time) + ' '
        print(timeArray)
    else:
        for x in xrange(0,len(textArray)):
            time += (difference / len(textArray))
            timeArray += str(time) + ' '

    # for all subtitle entries
    for x in xrange(1,entries):
        sub = subs[x]

        time = getTimeInMilliseconds(sub.start)
        end = getTimeInMilliseconds(sub.end)
        difference = end - time

        text = sub.text.replace('\n', ' ')
        textArray = text.split(' ')

        if overlap:
            fullText += ' ' + textArray[len(textArray) - 1]
            timeArray += str(end) + ' '
        else:
            fullText += ' ' + text
            for x in xrange(0,len(textArray)):
                time += (difference / len(textArray))
                timeArray += str(time) + ' '
    
    # remove tailing whitespace
    timeArray = timeArray[:-1]

    print(len(fullText.split(' ')))
    print(len(timeArray.split(' ')))
    if output:
        text_file = open(output, "w")
        text_file.write(fullText.encode('UTF-8'))
        text_file.write('\n\n')
        text_file.write(timeArray)
        text_file.close()

# Given a subtitle time entry, return the time value in milliseconds.
#
# @param subTime the subtitle time entry
#
# @return time value in milliseconds
#
def getTimeInMilliseconds(subTime):
    timeInMilliseconds = subTime.hours * 3600000
    timeInMilliseconds += subTime.minutes * 60000
    timeInMilliseconds += subTime.seconds * 1000
    timeInMilliseconds += subTime.milliseconds
    return timeInMilliseconds

if __name__ == '__main__':
    parseSrt()