import src.ascii_art_TNH.noises as noises
import src.ascii_art_TNH.gallery as gallery
from .noises import animal_noises #testing this

def ascii_art(user_input):
  # Type of the input-make sure string
  # Strip trailing spaces
  animal_array = parse_input(user_input)
  if len(animal_array) == 0:
    wrong_input("nothing", 0)
    return
  for animal in animal_array:
    # If animal is in the gallery
    if animal in gallery.animals:
      print_art(animal)
    elif animal in noises.animal_noises:
      print(print_art(get_noise(animal)))
    else:
      # If animal is not in the gallery
      wrong_input(animal, len(animal_array))

def parse_input(user_input):
  inputs = []
  inputs = user_input.split(" ")
  clean_input = []
  for input in inputs:
    if input != "" and input.isalpha():
      clean_input.append(input)
  return clean_input

def print_art(animal):
  #match animal with art
  #calls print_noise or wrong_input
  return(gallery.animals.get(animal))


def get_noise(noise):
   #match animal with noise

  # return(noises.get(noise))
  return animal_noises.get(noise)

def wrong_input(animals, length):
  #if multiple animals were inputed, print flowers
  #if one animal, print flower
  # reference: https://www.asciiart.eu/plants/flowers
  flowers = r"""
              ,,,                      ,,,
        {{{}}    ,,,             {{{}}    ,,,
      ,,, ~Y~    {{{}},,,      ,,, ~Y~    {{{}},,,
    {{}}} |/,,,  ~Y~{{}}}    {{}}} |/,,,  ~Y~{{}}}
      ~Y~ \|{{}}}/\|/ ~Y~  ,,, ~Y~ \|{{}}}/\|/ ~Y~  ,,,
      \|/ \|/~Y~  \|,,,|/ {{}}}\|/ \|/~Y~  \|,,,|/ {{}}}
      \|/ \|/\|/  \{{{}}/  ~Y~ \|/ \|/\|/  \{{{}}/  ~Y~
      \|/\\|/\|/ \\|~Y~//  \|/ \|/\\|/\|/ \\|~Y~//  \|/
      \|//\|/\|/,\\|/|/|// \|/ \|//\|/\|/,\\|/|/|// \|/
  jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  """
  flower = r""" 
               .-.'  '.-.
          .-(   \  /   )-.
         /   '..oOOo..'   \
 ,       \.--.oOOOOOOo.--./
 |\  ,   (   :oOOOOOOo:   )
_\.\/|   /'--'oOOOOOOo'--'\
'-.. ;/| \   .''oOOo''.   /
.--`'. :/|'-(   /  \   )-'
 '--. `. / //'-'.__.'-;
   `'-,_';//      ,  /|
        '((       |\/./_
          \\  . |\; ..-'
           \\ |\: .'`--.
            \\, .' .--'
             ))'_,-'`
       jgs  //-'
           // 
          //
         |/
  """
  if(length>1):
    return flowers
  else:
    return flower
  