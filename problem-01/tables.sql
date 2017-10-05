# this contains and creates a few simple tables to solve this design problem
# Please see the README.md and problem-01.md for more details

# The users who can post slide shows
CREATE TABLE Users (
    # could be UUID here too
    id INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id),

    # the name of the user, I'm not going to bother dealing with all the
    # permutations of a name (multiple middle names, one word only names, etc)
    name VARCHAR(255) NOT NULL,

    # email address of this user
    email VARCHAR(255) NOT NULL
);

# Represents a slideshow, which is a collection of slide items posted by some
# user on the site
CREATE TABLE SlideShowPost (
    # Another option for the id would be a UUID
    # However there is much debate _what_ should be used as a UUID, and if
    # Ids need to be UNIVERSALLY unique, or just unique to table their row
    # is in
    id INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id),

    # the user who posted this
    poster_id INT NOT NULL,
    FOREIGN KEY (poster_id)
        REFERENCES Users(id)
        ON DELETE CASCADE,

    # the title of the post
    title VARCHAR(255) NOT NULL,

    # the time this was originally posted
    post_date TIMESTAMP NOT NULL,

    # the last time this was edited
    edited_date TIMESTAMP
);

# Represents a slideshow, which is a collection of slide items posted by some
# user on the site
CREATE TABLE SlideItem (
    # could be UUID here too
    id INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id),

    # the slide show this item is a slide for
    slideshowpost_id INT NOT NULL,
    FOREIGN KEY (slideshowpost_id)
        REFERENCES SlideShowPost(id),

    # the ordering of the slide, so the first item would be 1, then second would
    # be 2, and so one and so forth
    ordering INT(8) NOT NULL,

    # the title of the slide item (displayed over image)
    title VARCHAR(255),

    # the text description, to preserve formatting maybe store the markdown here
    description TEXT NOT NULL,

    # the url to the image (assuming it's not stored in the DB too, probably on
    # some CDN somewhere, could change this to an ID to some table of CDN urls)
    image_url VARCHAR(255) NOT NULL,

    # optional source link
    source_url VARCHAR(255)
);
