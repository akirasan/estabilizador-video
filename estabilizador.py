import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Path de entrada")
parser.add_argument("-o", "--output", help="Path de salida")
args = parser.parse_args()

if args.input:
    print "path de entrada: ", args.input

if args.output:
    print "path de salida: ", args.output
else:
    args.output = args.input
    print "path de salida=entrada: ", args.output


#PASO 1
#ffmpeg -i test1.mp4 -vf vidstabdetect=stepsize=32:shakiness=10:accuracy=10:result=transforms.trf -f null -

#PASO 2
#ffmpeg -y -i test1.mp4 -vf vidstabtransform=input=transforms.trf:zoom=0:smoothing=10,unsharp=5:5:0.8:3:3:0.4 -vcodec libx264 -tune film -acodec copy -preset slow -an test2.mp4

for filename in os.listdir(args.input):
    if (filename.endswith(".MOV")): #or .avi, .mpeg, whatever.
        filename_sinext = os.path.splitext(filename)[0]
        print "================= Fichero: ", filename
        print "Paso 1 ================"
        os.system("ffmpeg -v warning -hide_banner -nostats -i {0} -vf vidstabdetect=stepsize=32:shakiness=10:accuracy=10:result={1}.trf -f null -".format(args.input+filename, args.output+filename_sinext))
        print "Paso 2 ================"
        os.system("ffmpeg -v warning -hide_banner -y -i {0} -vf vidstabtransform=input={1}.trf:zoom=0:smoothing=10,unsharp=5:5:0.8:3:3:0.4 -vcodec libx264 -tune film -acodec libmp3lame {2}.mp4".format(args.input+filename, args.output+filename_sinext, args.output+filename_sinext))
    else:
        continue

print "Finalizado\n"
