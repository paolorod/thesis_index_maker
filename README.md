# Thesis Index Maker


A simple project to help preparing the content index for French Law PHDs
It works as a command line utility from main.py

To see the help, run:

`python main.py -h`

## Prerequisite
As for French PHD's standards, we assume the requested index is based on paragraph number (and not page numbers).
We assume that
* The PHD is done via a recent version of Microsoft Word and saved in docx format
* Document styles have been used wisely. In particular, a style for the main paragraph text is used.  *This style is going to be used to create the index*

## Install
To install, you need Python 2.7 installed and setup.
Create a virtual environment is strongly advised.
After simply install the requirements via `pip install -r requirements.txt`

## To create the index
### Step 1 - Debug and optimize structure
As a first step, debug the document structure using the command

``python main.py -t debug -s <your style> <path-to-your-docx>``

This is going to create a modified word document that have:
 * in yellow all the text that is IGNORED for indexing. 
 * Next to each paragraph number another number added to the program based on its detection logic
 
 In order for the next steps to work properly, the document has to be modified in order that all the text outsite from the main corpus will be in yellow (titles, bibliography, dedicas etc.) and the numbers matches the number in word.
 This is normally done in a couple of iterations working on the styles
 
 ### Step 2 - Raw index
 Then you can produce a first raw index by running
 
 ``python main.py -t raw -s <your style> <path-to-your-docx> -o <output-path>``
 
 This creates a file with the most frequent word that are candidate for indexing in the form  word, <paragraphs>
 Is then the author's job as an expert of the field to reorganise those in a yaml file grouping them in sections, entries and specifications.
 
 This structure should be presented as a YAML file and saved for futher processing.
 As an example, here an extract of a yaml file with some extra comments added after `//`
 
 <pre>- Régime :  // section title
    - Régime :  // content entry with specification
      - Carcéral  // specification
      - Couvre-feu
      - Dérogatoire 
      - Différencié
      - Portes-fermées
      - Portes-ouvertes
      - Spécifique
      - Infantile
    - Verrouillage des portes // content entry
    - Mouvement 
 
 -  Commission consultative pluridisciplinaire :

- Juge des enfants :
  - Juge des enfants :
    - Compétence 
    - Saisine 
  - Maintien de l'enfant à dix-huit mois
  - Mesure d'assistance éducative
</pre>
 
 Note that:
 * If just the section title is specified, then it is used as a content entry
 * Specifications are searched aroun the content entry with specification
 * Synonims are not managed, so they should be added as entries
 
 
### Step 3 - Index Generation
Finally, as the structure is ready, you can run the final pass using

 ``python main.py -t structured -s <your style> -y <your-structure-file> <path-to-your-docx> -o <output-path>``
 