import hyperdiv as hd
from .registration_state import RegistrationState


"""
This is the header of the page.
Returns:
    Nothing, just render the elements 
Parameters:
    None
"""
def header():
    """
    TODO: The header containing a form and:
        1. A text input form where users will type the name of the pet
        2. A radio group where users will choose between dog or cat type 
        3. An "add" button that should only appear if the the user typed the name of a pet
        3.1 The "add button" should be a submit button for the form
        3.2 When the form is submitted, add the pet to the list of registrations 

    Style: 
    The form should be in a div box with style:
        1. Padding and gap equals to 1
        2. Alignment center
        3. Border in the bottom of 1px, solid and color neutral-200 

    The form style:
        1. Horizontal 
        2. Placeholder for text input: "Pet name?"
        3. Radio button style: default 

    Hints:
        1. Start the RegistrationState() class and use it to add new registrations
        2. Check if the form was submitted to trigger adding new registrations
        3. Give names to the form elements (text input and radio group) and use those
        names to access their values
    """
    pass



"""
This is a building block of the rendered list of registrations. 
Returns:
    Returns nothing, just render the elements 
Parameters:
    registration (string): name of the pet in the registration 
    pet_type (string): type of the pet (dog or cat)
    adopted (bool): whether the pet was adopted or not
    last_item (bool): whether this is the last item in the list of registrations
"""
def registration_row(registration,  pet_type, adopted, last_item=False):
    """
    TODO: this is the element registration row and it represents each one of
    the pets added in the RegistrationState(). This is a building block of the 
    rendered list of registrations. 
        1. Registration row should be a box (not a table). Dont use border if it's the 
        last item in the list of registrations. Otherwise, use 1px solid neutral-200
        2. Inside the box there shoud be a button that works as a toggle button
            2.1 If the pet was adopted, the button should be:
                2.1.1 Green green-50
                2.1.2 Have border 1px solid green-300
                2.1.3 Have a prefix icon called "check"
            2.2 Otherwise,if pet was not adopted 
                2.2.1 it should use default values for style
                2.2.2 have a prefix icon called of dot
        3. When button is clicked, it should be able to update/toggle the registration 
        of the pet in the registration list. 

        
    Hints:
        1. Initiate the RegistrationStates() to get the list of registrations 
        2. Update the registration of the pet using the initialized list and passing 
        the name of the pet (registration)
    """
    pass


"""
Building block for when there are no registrations to render. 
Returns:
    Returns nothing, just render the elements 
"""
def nothing_here():
    """
    TODO: This is rendered when there are no registrations to render.

    Contains just a box and a text inside. 
    Style:
        1. Box: padding of 1.5, align and justify should be centered
        2. Text:  color font "neutral-500"
        3. Text: "There are no pets here."
    """
    pass



"""
Renders the list of registrations or the nothing_here component if there are no registrations
Returns:
    Returns nothing, just render the elements 
"""
def registrations_list():
    """
    Renders the list of registrations; 
    or the nothing_here component if there are no registrations.

    1. Rendering should be inside a box with vertical scroll if there are registration items
    2. Otherwise, if there's not registration items just use the element nothing_here


    Hints:
        1. Initialize the registration list using RegistrationState()
        2. Loop through the registration items (pets) if there are any pets in the list 
        3. Call the registration_row() function to render each pet
            3.1 remember to use hd.scope() to render the registration of each row
        4. Call the nothing_here() function if there are no pets in the list
    """
    pass


def footer():
    """
    The footer, rendering the count of pets left, the nav
    """

    registrations = RegistrationState()

    with hd.hbox(
        justify="space-between",
        align="center",
        padding=1,
        height=3,
        border_top="1px solid neutral-200",
    ):
        # Count
        hd.text(
            f"{registrations.pets_left} pet{'s' if registrations.pets_left != 1 else ''} left",
            basis=0,
            grow=1,
        )

        with hd.box(basis=0, grow=1, align="end"):
            if registrations.has_completed:
                if hd.button("Clear list", size="small").clicked:
                    registrations.clear_completed()


def main():
    app = hd.template(title="Registration App", sidebar=False)
    app.body.align = "center"
    with app.body:
        with hd.box(
            background_color="neutral-50",
            border="1px solid neutral-200",
            width=40,
            border_radius="large",
            vertical_scroll=False,
        ):
            header()
            registrations_list()
            footer()