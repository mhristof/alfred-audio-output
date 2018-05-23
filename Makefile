#
#

alfred-audio.alfredworkflow: info.plist generate.py
	zip -r alfred-audio.alfredworkflow info.plist generate.py F58CE8B5-253D-472E-B7CB-7792978FB4AA.png icon.png

clean:
	rm -rf alfred-audio.alfredworkflow


# vim:ft=make
#
