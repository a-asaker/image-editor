# Image Editor:

   Edit Your Images Quickly With Python3 And OpenCV.

* You Can: 
     * Edit An Existing Image.
     * Create A New Image And Edit It.
     * Capture A Screenshot And Edit It.

* Editing Options:
        
     * Drawings:
          * Rectangles.
          * Circles.
          * Lines.
          * Free Drawing With A Mouse.
      
     * Adding Text.
     * Crop Image.
     * Colors:
          * Red
          * White
          * Black
          * Green
          * Cyan/Aqua
          * Blue
          * Pink
          * Orange
          * Yellow
     * Widths: From [1] To [9].
* Saveing Options: You Can Save Your Image As Png,JPG,JPEG,.. With The Name You Specify, The Default Is `Img.png`.

By : a-asaker.

# How To Run:

    Image Options/Arguments :
	  *[Open An Existing Image]:
		  -i,--image  <path>	: image path
	  *[Create A New Image]    :
  		-c,--create 		: crate a new image
  		-w,--width  <number>	: image width
  		-h,--height <number>	: image height
  		-b,--background <R,G,B> : image background color in RGB
  		<width, height, background are optional>
  	*[Capture A Screenshot]     :
  		-s,--screenshot		: capture a screenshot
  		-d,--delay		: time before capturing the screenshot
  		<delay is optional>
  	*[Output Options]:
  		-o,--output <name> : the name of the saved edited image
  		<output is optional>
    Examples:
	  ~ ./img_editor.py -i some_img.jpg
	  ~ ./img_editor.py -s
	  ~ ./img_editor.py -s -d 4
	  ~ ./img_editor.py -c
	  ~ ./img_editor.py -c --width 600 -h 500 -b 234,124,65
# How To Use:
* You Must Focus On The Image's Window First `Just Click On The Image To Be Able To Use Key Bindings`.

* This Project Works Through Key Striking And Mouse Events.
  
* Keys/Options : 
     
     Option/Mode| Key
     -----------|-----
     rectangle  | `r`
     line       | `l`
     draw       | `d`
     text       | `t`
     circle 	  | `c` `i`
     crop       | `c` `r`
     color      | `c` `o`
     width      | [`1`,`2`,`3`,..,`9`]
     save       | `s`
     undo crop  | `u`
     no mode    | `n`
     help       | `h`
     exit       | `esc`
     print mode | `m`
     print width| `w`
     
     Colors | Key
     -------|----
     red    | `r`
     green  | `g`
     white  | `w`
     yellow | `y`
     aqua/cyan| `a`
     pink   | `p`
     orange | `o`
     black  | `b` `k`
     blue   | `b` `l`
 
 * For Drawing/Crop Mode: Draw Using Drag-Drop [Drag At The Beginning Point, Drop At The Ending Point].
 
 * For Text Mode: Click On The Image At The Point You Want To Start Typing From, Then Start Typing. After Finishing Your Text Press `esc`.
     
