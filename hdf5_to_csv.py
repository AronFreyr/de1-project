#!/usr/bin/env python3
# coding: utf-8

# In[1]:


import time
import sys
import os
import glob
import hdf5_getters
import re
from os.path import exists

class Song:
    songCount = 0
    # songDictionary = {}

    def __init__(self, songID):
        
        
        # Song.songDictionary[songID] = self

        
#         self.genreList = []
        
#         self.lyrics = None
#         self.popularity = None
        
        self.id = songID
        Song.songCount += 1
        
        self.artistFamiliarity = ''
        self.artistHotttnesss = ''
        self.artistID = ''
        self.artistMbID = ''
        self.artistPlaymeId = ''
        self.artist7DigitalId = ''
        self.artistLatitude = ''
        self.artistLongitude = ''
        self.artistLocation = ''
        self.artistName = ''
        self.albumName = ''
        self.albumID = ''
        self.songHotttnesss = ''
        self.title = ''
        self.track7DigitalId = ''
        self.similarArtists = ''
        self.artistTerms = ''
        self.artistTermsFreq = ''
        self.artistTermsWeight = ''
        self.analysisSampleRate = ''
        self.audioMd5 = ''
        self.danceability = ''
        self.duration = ''
        self.endOfFadeIn = ''
        self.energy = ''
        self.keySignature = ''
        self.keySignatureConfidence = ''
        self.loudness = ''
        self.mode = ''
        self.modeConfidence = ''
        self.startOfFadeOut = ''
        self.tempo = ''
        self.timeSignature = ''
        self.timeSignatureConfidence = ''
        self.trackId = ''
        self.segmentsStart = ''
        self.segmentsConfidence = ''
        self.segmentsPitches = ''
        self.segmentsTimbre = ''
        self.segmentsLoudnessMax = ''
        self.segmentsLoudnessMaxTime = ''
        self.segmentsLoudnessStart = ''
        self.sectionsStart = ''
        self.sectionsConfidence = ''
        self.beatsStart = ''
        self.beatsConfidence = ''
        self.barsStart = ''
        self.barsConfidence = ''
        self.tatumsStart = ''
        self.tatumsConfidence = ''
        self.artistMbtags = ''
        self.artistMbtagsCount = ''
        self.year = ''
        
    def displaySongCount(self):
        print("Total Song Count {}".format(Song.songCount))

    def displaySong(self):
        print("ID: {}".format(self.id))   

def pretty_field_value(value):
    
    value = str(value)
    
    if len(value) == 3 and value == "b''":
        return ''
    elif len(value) > 3:
        value_start = value[0:2]
        value_end = value[-1]
        
        if value_start == "b'" and value_end == "'":
            return value[2:-1]
        else:
            return value
    else:
        return value

def pretty_array(input_array, pretty_value=False):
    
    return_str = ''
    
    for i in input_array:
        if pretty_value:
            return_str += '"' + pretty_field_value(i) + '" '
        else:
            return_str += '"' + str(i) + '" '
    
    return return_str
        
def pretty_2d_array(input_array, pretty_value=False):
    return_str = ''
    
    for j in input_array:
        for i in j:
            
            if pretty_value:
                return_str += pretty_field_value(i) + ' '
            else:
                return_str += str(i) + ' '
    
    return return_str

def main():
    
    write_to_csv_file = 'million_song_subset.csv'
    
    file_exists = exists(write_to_csv_file)
    
    outputFile1 = open(write_to_csv_file, 'a')
    csvRowString = ""

    #################################################
    #if you want to prompt the user for the order of attributes in the csv,
    #leave the prompt boolean set to True
    #else, set 'prompt' to False and set the order of attributes in the 'else'
    #clause
    prompt = False
    #################################################
    if prompt == True:
        while prompt:

            prompt = False

            csvAttributeString = raw_input("\n\nIn what order would you like the colums of the CSV file?\n" +
                "Please delineate with commas. The options are: " +
                "AlbumName, AlbumID, ArtistID, ArtistLatitude, ArtistLocation, ArtistLongitude,"+
                " ArtistName, Danceability, Duration, KeySignature, KeySignatureConfidence, Tempo," +
                " SongID, TimeSignature, TimeSignatureConfidence, Title, and Year.\n\n" +
                "For example, you may write \"Title, Tempo, Duration\"...\n\n" +
                "...or exit by typing 'exit'.\n\n")

            csvAttributeList = re.split('\W+', csvAttributeString)
            for i, v in enumerate(csvAttributeList):
                csvAttributeList[i] = csvAttributeList[i].lower()

            for attribute in csvAttributeList:
                # print "Here is the attribute: " + attribute + " \n"


                if attribute == 'AlbumID'.lower():
                    csvRowString += 'AlbumID'
                elif attribute == 'AlbumName'.lower():
                    csvRowString += 'AlbumName'
                elif attribute == 'ArtistID'.lower():
                    csvRowString += 'ArtistID'
                elif attribute == 'ArtistLatitude'.lower():
                    csvRowString += 'ArtistLatitude'
                elif attribute == 'ArtistLocation'.lower():
                    csvRowString += 'ArtistLocation'
                elif attribute == 'ArtistLongitude'.lower():
                    csvRowString += 'ArtistLongitude'
                elif attribute == 'ArtistName'.lower():
                    csvRowString += 'ArtistName'
                elif attribute == 'Danceability'.lower():
                    csvRowString += 'Danceability'
                elif attribute == 'Duration'.lower():
                    csvRowString += 'Duration'
                elif attribute == 'KeySignature'.lower():
                    csvRowString += 'KeySignature'
                elif attribute == 'KeySignatureConfidence'.lower():
                    csvRowString += 'KeySignatureConfidence'
                elif attribute == 'SongID'.lower():
                    csvRowString += "SongID"
                elif attribute == 'Tempo'.lower():
                    csvRowString += 'Tempo'
                elif attribute == 'TimeSignature'.lower():
                    csvRowString += 'TimeSignature'
                elif attribute == 'TimeSignatureConfidence'.lower():
                    csvRowString += 'TimeSignatureConfidence'
                elif attribute == 'Title'.lower():
                    csvRowString += 'Title'
                elif attribute == 'Year'.lower():
                    csvRowString += 'Year'
                elif attribute == 'Exit'.lower():
                    sys.exit()
                else:
                    prompt = True
                    print("==============")
                    print("I believe there has been an error with the input.")
                    print("==============")
                    break

                csvRowString += ","

            lastIndex = len(csvRowString)
            csvRowString = csvRowString[0:lastIndex-1]
            csvRowString += "\n"
            outputFile1.write(csvRowString);
            csvRowString = ""
    #else, if you want to hard code the order of the csv file and not prompt
    #the user, 
    else:
        
        #################################################
        #change the order of the csv file here
        #Default is to list all available attributes (in alphabetical order)
        csvRowString = ("song_id,artist_familiarity,artist_hotttnesss,artist_id,artist_mbid,artist_playmeid,"+
            "artist_7digitalid,artist_latitude,artist_longitude,artist_location,artist_name,"+
            "release,release_7digitalid,song_hotttnesss,title,track_7digitalid,similar_artists,artist_terms,"+
            "artist_terms_freq,artist_terms_weight,analysis_sample_rate,audio_md5,danceability,duration,end_of_fade_in,"+
            "energy,key,key_confidence,loudness,mode,mode_confidence,start_of_fade_out,tempo,time_signature,time_signature_confidence,"+
            "track_id,segments_start,segments_confidence,segments_pitches,segments_timbre,segments_loudness_max,segments_loudness_max_time,"+
            "segments_loudness_start,sections_start,sections_confidence,beats_start,beats_confidence,bars_start,bars_confidence,"+
            "tatums_start,tatums_confidence,artist_mbtags,artist_mbtags_count,year")
        #################################################

        csvAttributeList = re.split('\W+', csvRowString)
        
        if not file_exists:
            for i, v in enumerate(csvAttributeList):
                csvAttributeList[i] = csvAttributeList[i].lower()
            #outputFile1.write("SongNumber,");
            outputFile1.write(csvRowString + "\n");
        
        csvRowString = ""  

    #################################################


    #Set the basedir here, the root directory from which the search
    #for files stored in a (hierarchical data structure) will originate
    basedir = "MillionSongSubset" # "." As the default means the current directory
    ext = ".h5" #Set the extension here. H5 is the extension for HDF5 files.
    #################################################

    #FOR LOOP
    for root, dirs, files in os.walk(basedir):        
        files = glob.glob(os.path.join(root,'*'+ext))
        
        for f in files:
            print(f)

            h5 = hdf5_getters.open_h5_file_read(f)
            song = Song(str(pretty_field_value(hdf5_getters.get_song_id(h5))))

#             testDanceability = hdf5_getters.get_danceability(songH5File)
            # print type(testDanceability)
            # print ("Here is the danceability: ") + str(testDanceability)

#             song.artistID = str(hdf5_getters.get_artist_id(songH5File))
#             song.albumID = str(hdf5_getters.get_release_7digitalid(songH5File))
#             song.albumName = str(hdf5_getters.get_release(songH5File))
#             song.artistLatitude = str(hdf5_getters.get_artist_latitude(songH5File))
#             song.artistLocation = str(hdf5_getters.get_artist_location(songH5File))
#             song.artistLongitude = str(hdf5_getters.get_artist_longitude(songH5File))
#             song.artistName = str(hdf5_getters.get_artist_name(songH5File))
#             song.danceability = str(hdf5_getters.get_danceability(songH5File))
#             song.duration = str(hdf5_getters.get_duration(songH5File))
#             # song.setGenreList()
#             song.keySignature = str(hdf5_getters.get_key(songH5File))
#             song.keySignatureConfidence = str(hdf5_getters.get_key_confidence(songH5File))
#             # song.lyrics = None
#             # song.popularity = None
#             song.tempo = str(hdf5_getters.get_tempo(songH5File))
#             song.timeSignature = str(hdf5_getters.get_time_signature(songH5File))
#             song.timeSignatureConfidence = str(hdf5_getters.get_time_signature_confidence(songH5File))
#             song.title = str(hdf5_getters.get_title(songH5File))
#             song.year = str(hdf5_getters.get_year(songH5File))

            
            song.artistFamiliarity = str(hdf5_getters.get_artist_familiarity(h5))
            song.artistHotttnesss = str(hdf5_getters.get_artist_hotttnesss(h5))
            song.artistID = str(pretty_field_value(hdf5_getters.get_artist_id(h5)))
            song.artistMbID = str(pretty_field_value(hdf5_getters.get_artist_mbid(h5)))
            song.artistPlaymeId = str(pretty_field_value(hdf5_getters.get_artist_playmeid(h5)))
            song.artist7DigitalId = str(hdf5_getters.get_artist_7digitalid(h5))
            song.artistLatitude = str(hdf5_getters.get_artist_latitude(h5))
            song.artistLongitude = str(hdf5_getters.get_artist_longitude(h5))
            song.artistLocation = str(pretty_field_value(hdf5_getters.get_artist_location(h5)))
            song.artistName = str(pretty_field_value(hdf5_getters.get_artist_name(h5)))
            song.albumName = str(pretty_field_value(hdf5_getters.get_release(h5)))
            song.albumID = str(hdf5_getters.get_release_7digitalid(h5))
            song.songHotttnesss = str(hdf5_getters.get_song_hotttnesss(h5))
            song.title = str(pretty_field_value(hdf5_getters.get_title(h5)))
            song.track7DigitalId = str(hdf5_getters.get_track_7digitalid(h5))
            #song.similarArtists = str(pretty_array(hdf5_getters.get_similar_artists(h5), True))
            song.artistTerms = str(pretty_array(hdf5_getters.get_artist_terms(h5), True))
            #song.artistTermsFreq = str(pretty_array(hdf5_getters.get_artist_terms_freq(h5)))
            #song.artistTermsWeight = str(pretty_array(hdf5_getters.get_artist_terms_weight(h5)))
            song.analysisSampleRate = str(hdf5_getters.get_analysis_sample_rate(h5))
            song.audioMd5 = str(pretty_field_value(hdf5_getters.get_audio_md5(h5)))
            song.danceability = str(hdf5_getters.get_danceability(h5))
            song.duration = str(hdf5_getters.get_duration(h5))
            song.endOfFadeIn = str(hdf5_getters.get_end_of_fade_in(h5))
            song.energy = str(hdf5_getters.get_energy(h5))
            song.keySignature = str(hdf5_getters.get_key(h5))
            song.keySignatureConfidence = str(hdf5_getters.get_key_confidence(h5))
            song.loudness = str(hdf5_getters.get_loudness(h5))
            song.mode = str(hdf5_getters.get_mode(h5))
            song.modeConfidence = str(hdf5_getters.get_mode_confidence(h5))
            song.startOfFadeOut = str(hdf5_getters.get_start_of_fade_out(h5))
            song.tempo = str(hdf5_getters.get_tempo(h5))
            song.timeSignature = str(hdf5_getters.get_time_signature(h5))
            song.timeSignatureConfidence = str(hdf5_getters.get_time_signature_confidence(h5))
            song.trackId = str(pretty_field_value(hdf5_getters.get_track_id(h5)))
            #song.segmentsStart = str(pretty_array(hdf5_getters.get_segments_start(h5)))
            #song.segmentsConfidence = str(pretty_array(hdf5_getters.get_segments_confidence(h5)))
            #song.segmentsPitches = str(pretty_2d_array(hdf5_getters.get_segments_pitches(h5)))
            #song.segmentsTimbre = str(pretty_2d_array(hdf5_getters.get_segments_timbre(h5)))
            #song.segmentsLoudnessMax = str(pretty_array(hdf5_getters.get_segments_loudness_max(h5)))
            #song.segmentsLoudnessMaxTime = str(pretty_array(hdf5_getters.get_segments_loudness_max_time(h5)))
            #song.segmentsLoudnessStart = str(pretty_array(hdf5_getters.get_segments_loudness_start(h5)))
            #song.sectionsStart = str(pretty_array(hdf5_getters.get_sections_start(h5)))
            #song.sectionsConfidence = str(pretty_array(hdf5_getters.get_sections_confidence(h5)))
            #song.beatsStart = str(pretty_array(hdf5_getters.get_beats_start(h5)))
            #song.beatsConfidence = str(pretty_array(hdf5_getters.get_beats_confidence(h5)))
            #song.barsStart = str(pretty_array(hdf5_getters.get_bars_start(h5)))
            #song.barsConfidence = str(pretty_array(hdf5_getters.get_bars_confidence(h5)))
            #song.tatumsStart = str(pretty_array(hdf5_getters.get_tatums_start(h5)))
            #song.tatumsConfidence = str(pretty_array(hdf5_getters.get_tatums_confidence(h5)))            
            #song.artistMbtags = str(pretty_array(hdf5_getters.get_artist_mbtags(h5), True))
            #song.artistMbtagsCount = str(pretty_array(hdf5_getters.get_artist_mbtags_count(h5)))
            
            song.year = str(hdf5_getters.get_year(h5))
        
            #print song count
            #csvRowString += str(song.songCount) + ","

            for attribute in csvAttributeList:
                # print "Here is the attribute: " + attribute + " \n"

                if attribute == 'song_id':
                    csvRowString += "\"" + song.id + "\""
                elif attribute == 'artist_familiarity':
                    csvRowString += song.artistFamiliarity
                elif attribute == 'artist_hotttnesss':
                    csvRowString += song.artistHotttnesss
                elif attribute == 'artist_id':
                    csvRowString += "\"" + song.artistID + "\""
                elif attribute == 'artist_mbid':
                    csvRowString += song.artistMbID
                elif attribute == 'artist_playmeid':
                    csvRowString += song.artistPlaymeId
                elif attribute == 'artist_7digitalid':
                    csvRowString += song.artist7DigitalId
                elif attribute == 'artist_latitude':
                    latitude = song.artistLatitude
                    if latitude == 'nan':
                        latitude = ''
                    csvRowString += latitude
                elif attribute == 'artist_longitude':
                    longitude = song.artistLongitude
                    if longitude == 'nan':
                        longitude = ''
                    csvRowString += longitude
                elif attribute == 'artist_location':
                    location = song.artistLocation
                    location = location.replace(',','')
                    csvRowString += "\"" + location + "\""
                elif attribute == 'artist_name':
                    csvRowString += "\"" + song.artistName + "\""
                elif attribute == 'release':
                    albumName = song.albumName
                    albumName = albumName.replace(',',"")
                    csvRowString += "\"" + albumName + "\""
                elif attribute == 'release_7digitalid':
                    csvRowString += song.albumID
                elif attribute == 'song_hotttnesss':
                    csvRowString += song.songHotttnesss
                elif attribute == 'title':
                    csvRowString += "\"" + song.title + "\""
                elif attribute == 'track_7digitalid':
                    csvRowString += song.track7DigitalId
                elif attribute == 'similar_artists':
                    csvRowString += song.similarArtists
                elif attribute == 'artist_terms':
                    csvRowString += song.artistTerms
                elif attribute == 'artist_terms_freq':
                    csvRowString += song.artistTermsFreq
                elif attribute == 'artist_terms_weight':
                    csvRowString += song.artistTermsWeight
                elif attribute == 'analysis_sample_rate':
                    csvRowString += song.analysisSampleRate
                elif attribute == 'audio_md5':
                    csvRowString += song.audioMd5
                elif attribute == 'danceability':
                    csvRowString += song.danceability
                elif attribute == 'duration':
                    csvRowString += song.danceability
                elif attribute == 'end_of_fade_in':
                    csvRowString += song.endOfFadeIn
                elif attribute == 'energy':
                    csvRowString += song.energy
                elif attribute == 'key':
                    csvRowString += song.keySignature
                elif attribute == 'key_confidence':
                    csvRowString += song.keySignatureConfidence
                elif attribute == 'loudness':
                    csvRowString += song.loudness
                elif attribute == 'mode':
                    csvRowString += song.mode
                elif attribute == 'mode_confidence':
                    csvRowString += song.modeConfidence
                elif attribute == 'start_of_fade_out':
                    csvRowString += song.startOfFadeOut
                elif attribute == 'tempo':
                    csvRowString += song.tempo
                elif attribute == 'time_signature':
                    csvRowString += song.timeSignature
                elif attribute == 'time_signature_confidence':
                    csvRowString += song.timeSignatureConfidence
                elif attribute == 'track_id':
                    csvRowString += song.trackId
                elif attribute == 'segments_start':
                    csvRowString += song.segmentsStart
                elif attribute == 'segments_confidence':
                    csvRowString += song.segmentsConfidence
                elif attribute == 'segments_pitches':
                    csvRowString += song.segmentsPitches
                elif attribute == 'segments_timbre':
                    csvRowString += song.segmentsTimbre
                elif attribute == 'segments_loudness_max':
                    csvRowString += song.segmentsLoudnessMax
                elif attribute == 'segments_loudness_max_time':
                    csvRowString += song.segmentsLoudnessMaxTime
                elif attribute == 'segments_loudness_start':
                    csvRowString += song.segmentsLoudnessStart
                elif attribute == 'sections_start':
                    csvRowString += song.sectionsStart
                elif attribute == 'sections_confidence':
                    csvRowString += song.sectionsConfidence
                elif attribute == 'beats_start':
                    csvRowString += song.beatsStart
                elif attribute == 'beats_confidence':
                    csvRowString += song.beatsConfidence
                elif attribute == 'bars_start':
                    csvRowString += song.barsStart
                elif attribute == 'bars_confidence':
                    csvRowString += song.barsConfidence
                elif attribute == 'tatums_start':
                    csvRowString += song.tatumsStart
                elif attribute == 'tatums_confidence':
                    csvRowString += song.tatumsConfidence
                elif attribute == 'artist_mbtags':
                    csvRowString += song.artistMbtags
                elif attribute == 'artist_mbtags_count':
                    csvRowString += song.artistMbtagsCount
                elif attribute == 'year':
                    csvRowString += song.year
                
                
#                 if attribute == 'AlbumID'.lower():
#                     csvRowString += song.albumID
#                 elif attribute == 'AlbumName'.lower():
#                     albumName = song.albumName
#                     albumName = albumName.replace(',',"")
#                     csvRowString += "\"" + albumName + "\""
#                 elif attribute == 'ArtistID'.lower():
#                     csvRowString += "\"" + song.artistID + "\""
#                 elif attribute == 'ArtistLatitude'.lower():
#                     latitude = song.artistLatitude
#                     if latitude == 'nan':
#                         latitude = ''
#                     csvRowString += latitude
#                 elif attribute == 'ArtistLocation'.lower():
#                     location = song.artistLocation
#                     location = location.replace(',','')
#                     csvRowString += "\"" + location + "\""
#                 elif attribute == 'ArtistLongitude'.lower():
#                     longitude = song.artistLongitude
#                     if longitude == 'nan':
#                         longitude = ''
#                     csvRowString += longitude                
#                 elif attribute == 'ArtistName'.lower():
#                     csvRowString += "\"" + song.artistName + "\""                
#                 elif attribute == 'Danceability'.lower():
#                     csvRowString += song.danceability
#                 elif attribute == 'Duration'.lower():
#                     csvRowString += song.duration
#                 elif attribute == 'KeySignature'.lower():
#                     csvRowString += song.keySignature
#                 elif attribute == 'KeySignatureConfidence'.lower():
#                     # print "key sig conf: " + song.timeSignatureConfidence                                 
#                     csvRowString += song.keySignatureConfidence
#                 elif attribute == 'SongID'.lower():
#                     csvRowString += "\"" + song.id + "\""
#                 elif attribute == 'Tempo'.lower():
#                     # print "Tempo: " + song.tempo
#                     csvRowString += song.tempo
#                 elif attribute == 'TimeSignature'.lower():
#                     csvRowString += song.timeSignature
#                 elif attribute == 'TimeSignatureConfidence'.lower():
#                     # print "time sig conf: " + song.timeSignatureConfidence                                   
#                     csvRowString += song.timeSignatureConfidence
#                 elif attribute == 'Title'.lower():
#                     csvRowString += "\"" + song.title + "\""
#                 elif attribute == 'Year'.lower():
#                     csvRowString += song.year
#                 else:
#                     csvRowString += "Erm. This didn't work. Error. :( :(\n"

                csvRowString += ","

            #Remove the final comma from each row in the csv
            lastIndex = len(csvRowString)
            csvRowString = csvRowString[0:lastIndex-1]
            csvRowString += "\n"
            outputFile1.write(csvRowString)
            csvRowString = ""

            h5.close()
            
            # delete the file as it has converted
            os.remove(f)

    outputFile1.close()

start = time.time()
main()
end = time.time()
print(end - start)


# In[ ]:




