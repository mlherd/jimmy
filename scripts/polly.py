#!/usr/bin/env python
import subprocess

command = 'aws polly synthesize-speech --text-type ssml --text "<speak>Hey Gabi! I am so ready to be programmed to do great things! and attacking is not one of them</speak>" --output-format mp3 --voice-id Justin /home/melih/Desktop/speech.mp3'

file_name = 'polly_out.mp3'
subprocess.call(command, shell=True)