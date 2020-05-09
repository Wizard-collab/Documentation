^^^^^^^^
Overview
^^^^^^^^


Menu
====

Wizard
^^^^^^

The “About” tab of the Wizard menu contains the Version and the Wizard License information.
Access the Wizard - Pipeline Manager project hosted by Github

.. image:: _images/overview_menu_1.png
  :width: 300
  :alt: Alternative text


Project
^^^^^^^
	
The “Project” tab allows you to manage your projects. Create, open, change, and configure all your projects from this menu.

.. image:: _images/overview_menu_2.png
  :width: 300
  :alt: Alternative text


User
^^^^
	
The “User” tab allows you to manage registered users in wizard. Create, change, and set your password from this menu.

.. image:: _images/overview_menu_3.png
  :width: 300
  :alt: Alternative text


Settings
^^^^^^^^

The “Settings” tab allows you to set each software to your liking: add the path of the “.exe”, environment variables and scripts via “Softwares”.

.. image:: _images/overview_menu_4.png
  :width: 300
  :alt: Alternative text

Customize the interface and the various features of the UI Wizard from “Settings” tab of the settings menu. These settings are user preferences and project-independent.


Tools
^^^^^

Viewer : Wizard adapts its UI according to the preference files generated when the user create an asset, publish an asset, etc... These files are created automatically when you work and are only available for reading and editing in the “Viewer” tool. 

.. danger::
	Modifying these files can corrupt a whole part of your pipeline, it’s strongly recommended to edit them only with full knowledge.


Subprocess manager : The Subprocess Manager is a tool that isolates and relocates some wizard tasks. It allows you to keep using Wizard while it performs long and incompressible operations like publish and map conversation, playblast or animation export.


PyWizard : Access subprocess application programming interface.

.. image:: _images/overview_menu_5.png
  :width: 300
  :alt: Alternative text


Help
^^^^

In this tab, access to the Wizard updates, documentation and python API. In case of problems, write to the technical support from “Contact”.

.. image:: _images/overview_menu_6.png
  :width: 300
  :alt: Alternative text



Outliner
========


The Outliner allows you to create and archive assets and stages.
The outliner is connected to your project. It contains and lists all the scenes and allows you to intuitively access on every file of your project. Each user connected to the project will access to the outliner and its functions. The search function saves if your project contains a large volume of assets.

.. image:: _images/overview_outliner_1.png
  :width: 800
  :alt: Alternative text

	
Assets
^^^^^^

The “Asset” block of the Outliner contains all your assets. Divided into four categories: Characters, Vehicles, Set, Set Dress.
Each Asset contains a specific list of stages. They represent the fabrication process of the asset: Design, Modeling, Rigging, Grooming, Texturing, Shading.

.. image:: _images/overview_outliner_2.png
  :width: 800
  :alt: Alternative text


Library
^^^^^^^

The “Library” block contains specific and recurring assets of your project. Camera Rig, Auto Rig, Scripts, Gizmo, Shaders, etc... all available and referenceable in your scenes once created and published.

.. image:: _images/overview_outliner_3.png
  :width: 800
  :alt: Alternative text


Sequence
^^^^^^^^

The “Sequence” block contains all your animated scenes, from concept stages to lighting. Create a technical or definitive sequence, set the name and number of images of each shot.

.. image:: _images/overview_outliner_4.png
  :width: 800
  :alt: Alternative text


Editing
^^^^^^^

The “Editing” block is divided into two categories: Videos and Sound. As the previous bloc, it gives an access to your post production scenes.

.. image:: _images/overview_outliner_5.png
  :width: 800
  :alt: Alternative text



Scene 
=====


Node Graph
^^^^^^^^^^

The Node Graph is a nodal representation of the content of your work scene. Your work file is represented by a node relative to the stage to which it corresponds. This is the central node of the Graph Node, separated from the other nodes. If your file is a modeling file, it will be represented by a modeling node, etc...
The other nodes represents the references in your scene.

-- image-- (Node Graph contenant 3 REFS - Node Graph HL, main Node HL et commentée “Main Node”, Refs HL commentées “Références”)


List Jobs
^^^^^^^^^

The job list tab is a list presentation of the content of the Node Graph.

-- image-- (List Job - List Job HL)


Exports
^^^^^^^

The “Exports” tab lists all the export history of your scene. You can open or comment any export using the icons on the right side.

-- image-- (Export - Export Onglet HL et les icones explorer/comment sous lignées)


Work versions
^^^^^^^^^^^^^

The “Work Version” tab lists all the versions history of your scene. You can open, comment or delete any version using the icons on the right side.

-- image-- (Work versions - Work versions HL + les icones explorer, delete et comment sous lignées)


Playblast
^^^^^^^^^

The “Playblast” tab lists all playblast history. You can open, launch or delete any Playblast file using the icons on the right side. At any time, you can ask Wizard for a playblast of the scene using the “Playblast” button at the bottom right.

-- image-- (Playblast - Playblast HL + les icones explorer, delete et launch sous lignées + bouton Playblast HL )


History
^^^^^^^

The “History” tab displays the history of the asset from its creation to its last modification.

-- image-- (History - History HL)


Tickets
^^^^^^^

The “Ticket” tab allows you to open a ticket on an asset. A ticket is a note that reveals a problem and justifies a retake. Choose the user concerned and create the ticket. Once opened on the asset, the concerned user will receive a notification: the ticket will remain open until a user close it.

-- image-- (Tickets - Tickets HL)



Launcher
========


The Launcher is the area where you select the variant and version of an asset and then the software you are working with. This is also where you access the comments and screenshot of your scenes.


Variants
^^^^^^^^

By default, each asset is created on a variant called “main”. This is the asset in its main variant. Variants are each of the differences represented by a replica or a copy of the main asset in its main variant.
The variants of an asset simplify the integration of these differences in the pipeline of the concerned asset. You can create as many variants as the asset requires for your project. 
For example, variants are used in case of clothing changes for a character. This example therefore implies a variant of the asset in the modeling, texturing, rig and shading stages to integrate these differences into your project. Another variant example: If the texturing of your asset changes, a variant in the texturing stage is necessary.

-- image-- (Launcher, Section variante déroulé avec plusieur variantes ( claire dans le meilleur des cas)


Softwares
^^^^^^^^^

The “softwares” part of the launcher allows you to choose the software you want to use to work on the selected asset’s stage.

-- image-- (Softwares List Launcher déroulé HL)


Version
^^^^^^^

The version of the asset (not to be confused with the variant of an asset) is the backup history of your asset. By default, an asset is created in version 0000, each backup increments this numbers as follows: 0001, 0002, 0003 etc... 
A list containing these versions is available in selection in this part of the launcher and allows you to open any working version of your asset.

-- image-- (Menu Version déroulé - HL)


Comment
^^^^^^^

The comment section of the Launcher allows you to comment each working version. Version comments are very useful for the fabrication history of an asset. They are even more useful during a version back-up to know on which version you want to perform this back-up. Use the comments to document the history of your asset. Write in the text field and click the comment icon to post your comment.

-- image-- (Comment section avec commentaire inscrit dedans )


Screenshot
^^^^^^^^^^

The screenshot of your work scene is done when you save your asset in the software. It allows to display an image of the scene and helps visualise your asset without opening it.

-- image-- (Screenshot scene )


Locker
^^^^^^

The locker is a function that locks an asset automatically when it is opened from Wizard. This function aims to secure the working scene so that each file is edited by one user at a time. Once your work is complete, the asset remains locked and therefore unavailable to the rest of your team. Remember to unlock it by clicking on the locker icon. If you are looking to unlock a working scene locked by an absent user that can’t do it itself, you can right click on the locker icon and select “send unlock request”. This function sends a code per email to the user who locked the scene. Get the code from this user and write it in the text box provided for this purpose so that wizard unlocks the scene. This process ensures that the user who owns the lock allows you access to the file.

-- image-- (Lock)


Launcher
^^^^^^^^

The Launcher allows you to open your work scenes, it’s the only way to open your software and recover the Wizard tools that will allow it to integrate your work into the pipeline. The launcher opens the variant and its selected version, with the selected software.

-- image-- (Launcher)


User infos
==========


It’s here in the UI that you will find information about your user. Your photo, your level, your Xps.
Xps is earned by the work done from Wizard. Levels are earned from Xps. 
This is also where the administrator status is mentioned, if you declared yourself as administrator when you created your user.
You can also consult the tickets that are sent to you and the notifications you are sending.

--image-- (User Infos)


Quotes & Jokes
==============

This part of the Wizard UI allows users to add text that will be displayed randomly. Click the “+” button and add your message. You can also rate from 1 to 5 stars all messages except yours .

--image-- (Jokes)


Project & Machine infos
=======================


This part shows you which project is connected to Wizard as well as its location.
It also shows the performance of your machine in real time.

.. image:: _images/overview_project_machine_1.png
  :width: 800
  :alt: Alternative text


Extras
======

Extras tools are represented by icons at the bottom right of the Wizard interface.

--image-- ( all icones extras )

Notification Wall
^^^^^^^^^^^^^^^^^

The Notifications Wall allows you to have an overview of your project history through notifications. You can filter and display only “Create”, “Publish” and “Remove” notifications.

-- image-- (Notification Wall + icône en bas à droite)


Chat
^^^^

The chat is an internal communication system hosted on the Wizard server. It allows to communicate in real time with users connected to the project. You can also use it to send images to your team.

-- image-- (Chat + icône en bas à droite)


Python Console & Log 
^^^^^^^^^^^^^^^^^^^^

The wizard python console allows you to execute python commands. This is where the wizard log is located. If any error occurs while using Wizard, click the mail icon on the console to send the Error Log to the Wizard support team.

-- image-- (Console et mail icon + icône en bas à droite)


Locked Asset
^^^^^^^^^^^^

This button allows you to see the number of assets locked by your user and unlock them directly with one click. To allow other users to open any work scene of the project in your absence, it’s strongly recommended to unlock your assets through this button, before quitting your Wizard session.

-- image-- (UI Locked Asset + icône en bas à droite)


Running Asset
^^^^^^^^^^^^^

This button allows you to see the number of assets in work if you have multiples opened scenes.

-- image-- (UI Running Asset + icône en bas à droite)


