import datajoint as dj

schema = dj.schema(dj.config.get('database.prefix') + 'churchland_common_lab')

@schema
class Monkey(dj.Lookup):
    definition = """
    monkey:    varchar(32)    # monkey name
    ---
    monkey_id: int unsigned   # monkey ID number
    sex:       enum('M', 'F') # monkey sex
    dob:       date           # monkey date of birth
    """
    
    contents = [
        ['Drake',    37468, 'M', '2006-05-01'],
        ['Cousteau', 35946, 'M', '2004-05-19'],
        ['Balboa',   33958, 'M', '2002-04-11'],
        ['Alex',     37335, 'M', '2006-04-15'],
        ['Gimli',    39837, 'M', '2009-05-04'],
        ['Hudson',   40344, 'M', '2009-06-10'],
        ['Igor',     39914, 'M', '2009-04-11'],
        ['Eugustus', 1196,  'M', '1999-01-01']
    ]

    
@schema
class Rig(dj.Lookup):
    definition = """
    # Experimental rigs
    rig: varchar(16) # rig name
    """
    
    contents = [
        ['Fangorn'],
        ['Jumanji'],
        ['Krypton']
    ]


@schema
class User(dj.Lookup):
    definition = """
    user_uni: varchar(32)  # user uni
    ---
    user:     varchar(255) # user name (first and last)
    """
    
    contents = [
        ['arw2212', 'Adam Wilke'],
        ['emt2177', 'Eric Trautmann'],
        ['njm2149', 'Najja Marshall']
    ]