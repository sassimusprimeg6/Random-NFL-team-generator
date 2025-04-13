import random

def random_image_path():
    # Create a dictionary mapping numbers to image paths
    image_paths = {
        1: "team_images/49ers.png",
        2: "team_images/bears.png",
        3: "team_images/bengals.png",
        4: "team_images/bills.png",
        5: "team_images/broncos.png",
        6: "team_images/browns.png",
        7: "team_images/buccaneers.png",
        8: "team_images/cardinals.png",
        9: "team_images/chargers.png",
        10: "team_images/chiefs.png",
        11: "team_images/colts.png",
        12: "team_images/commanders.png",
        13: "team_images/cowboys.png",
        14: "team_images/dolphins.png",
        15: "team_images/eagles.png",
        16: "team_images/falcons.png",
        17: "team_images/giants.png",
        18: "team_images/jaguars.png",
        19: "team_images/jets.png",
        20: "team_images/lions.png",
        21: "team_images/packers.png",
        22: "team_images/panthers.png",
        23: "team_images/patriots.png",
        24: "team_images/raiders.png",
        25: "team_images/rams.png",
        26: "team_images/ravens.png",
        27: "team_images/saints.png",
        28: "team_images/seahawks.png",
        29: "team_images/steelers.png",
        30: "team_images/texans.png",
        31: "team_images/titans.png",
        32: "team_images/vikings.png"
    }
    
    # Generate a random number between 1 and 32
    random_number = random.randint(1, 32)
    
    # Get the image path corresponding to the random number
    selected_image = image_paths[random_number]
    print(f"Randomly selected image path: {selected_image}")

# Call the function
random_image_path()
