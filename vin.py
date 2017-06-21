vin = '1FBVU4XG0FKA02238'


# Item Description 
# 1 WMI (World Manufacturer Identifier) 
# 2 Restraint-type and GVW code 
# 3 Vehicle line, series, body-type code 
# 4 Engine-type code 
# 5 Computer-generated check digit 
# 6 Model year code 
# 7 Assembly plant code 
# 8 Production sequence number 

lookup = {
  'wmi': {'1FB': 'Ford Motor Company, USA, wagon',  
        '1FD': 'Ford Motor Company, USA, incomplete vehicle',
        '1FM': 'Ford Motor Company, USA, multi-purpose vehicle (MPV)',
        '1FT': 'Ford Motor Company, USA, truck (complete vehicle)'},
  'restraint': {'A': '9,001-10,000 lb GVW , active safety belts (all positions), driver and front passenger air bags - 1st, 2nd and 3rd row side inflatable restraints',
              'B': '9,001-10,000 lb GVW , active safety belts (all positions), driver and front passenger air bags - 1st row side inflatable restraints',
              'C': '8,501-9,000 lb GVW , active safety belts (all positions), driver air bag',
              'D': '9,001-10,000 lb GVW , active safety belts (all positions) with driver side air bag',
              'E': '10,001-14,000 lb GVW , active safety belts (all positions) with driver side air bag',
              'F': '8,501-9,000 lb GVW , active safety belts (all positions), driver air bag - 1st, 2nd and 3rd row side inflatable restraints',
              'G': '9,001-10,000 lb GVW , active safety belts (all positions), driver air bag - 1st, 2nd and 3rd row side inflatable restraints',
              'H': '10,001-14,000 lb GVW , active safety belts (all positions), driver air bag - 1st, 2nd and 3rd row side inflatable restraints',
              'K': '8,501-9,000 lb GVW , active safety belts (all positions), driver air bag - 1st row side inflatable restraints',
              'L': '9,001-10,000 lb GVW , active safety belts (all positions), driver air bag - 1st row side inflatable restraints',
              'M': '10,001-14,000 lb GVW , active safety belts (all positions), driver air bag - 1st row side inflatable restraints',
              'N': '8,501-9,000 lb GVW , active safety belts (all positions) with driver and front passenger air bags',
              'R': '10,001-14,000 lb GVW , active safety belts (all positions), driver and front passenger air bags - 1st row side inflatable restraints',
              'S': '9,001-10,000 lb GVW , active safety belts (all positions) with driver and front passenger air bags',
              'V': '10,001-14,000 lb GVW , active safety belts (all positions), driver and front passenger air bags - 1st, 2nd and 3rd row side inflatable restraints',
              'W': '10,001-14,000 lb GVW , active safety belts (all positions) with driver and front passenger air bags',
              'Y': '8,501-9,000 lb GVW , active safety belts (all positions), driver and front passenger air bags - 1st row side inflatable restraints',
              'Z': '8,501-9,000 lb GVW , active safety belts (all positions), driver and front passenger air bag - 1st, 2nd and 3rd row side inflatable restraints'},
  'body': {'E1C': 'Transit, medium roof line, RH side sliding load door, cargo van 129 in wheelbase), 390M series',
        'E1D': 'Transit, medium roof line, dual side sliding load doors, cargo van (129 in wheelbase), 309M series',
        'E1Y': 'Transit, medium-low roof line, RH side sliding load door, cargo van (129 in wheelbase), 390M series',
        'E1Z': 'Transit, medium-low roof line, RH side swinging load doors, cargo van (129 in wheelbase), 390M series',
        'E2C': 'Transit, medium roof line, RH side sliding load door, cargo van (148 in wheelbase), 390L series',
        'E2D': 'Transit, medium roof line, dual sliding load doors, cargo van (148 in wheelbase), 390L series',
        'E2Y': 'Transit, medium-low roof line, RH side sliding load door, cargo van (148 in wheelbase), 390L series',
        'E9Z': 'Transit, medium-low roof line, RH side swinging load door, cargo van (148 in wheelbase), 390L series',
        'F4U': 'Transit, high roof line, dual sliding side load doors, cargo van (148 in wheelbase), dual rear wheels, 450E series',
        'F4X': 'Transit, high roof line, RH side sliding load door, cargo van (148 in wheelbase), dual rear wheels, 450E series',
        'F6P': 'Transit, cutaway (138 in wheelbase), dual rear wheels, 450M series',
        'F6Z': 'Transit, regular cab (138 in wheelbase), dual rear wheels, 450M series',
        'F8P': 'Transit, cutaway (156 in wheelbase), dual rear wheels, 450L series',
        'F8Z': 'Transit, regular cab (156 in wheelbase), dual rear wheels, 450L series',
        'F9P': 'Transit, cutaway (178 in wheel base), dual rear wheels, 450EL series',
        'F9Z': 'Transit, regular cab (178 in wheelbase), dual rear wheels, 450EL series',
        'K1C': 'Transit, medium-low roof line, RH side sliding load door, wagon (129 in wheelbase), 390M series',
        'K1Y': 'Transit, medium-low roof line, RH side sliding load door, wagon (129 in wheelbase), 390M series',
        'K1Z': 'Transit, medium-low roof line, RH side swinging load door, wagon (129 in wheelbase), 390M series',
        'R1C': 'Transit, medium roof line, RH side sliding load door, cargo van (129 in wheelbase), 410M series',
        'R1D': 'Transit, medium roof line, dual sliding load doors, cargo van (129 in wheelbase), 410M series',
        'R1Y': 'Transit, medium-low roof line, RH side sliding load door, cargo van (129 in wheelbase), 410M series',
        'R1Z': 'Transit, medium-low roof line, RH side swinging load doors, cargo van (129 in wheelbase), 410M series',
        'R2C': 'Transit, medium roof line, RH side sliding load door, cargo van (148 in wheelbase), 410L series',
        'R2D': 'Transit, medium roof line, dual sliding load doors, cargo van (148 in wheelbase), 410L series',
        'R2U': 'Transit, high roof line, dual sliding load doors, cargo van (148 in wheelbase), 410L series',
        'R2X': 'Transit, high roof line, RH side sliding load door, cargo van (148 in wheelbase), 410L series',
        'R2Y': 'Transit, medium-low roof line, RH side sliding load door, cargo van (148 in wheelbase), 410L series',
        'R2Z': 'Transit, medium-low roof line, RH side swinging load doors, cargo van (148 in wheelbase), 410L series',
        'R3U': 'Transit, high roof line, dual sliding load doors, cargo van (148 in wheelbase), 410E series',
        'R3X': 'Transit, high roof line, RH side sliding load door, cargo van (148 in wheelbase), 410E series',
        'R5P': 'Transit, cutaway (138 in wheelbase), dual rear wheels, 410M series',
        'R5Z': 'Transit, regular cab (138 in wheelbase), 410M series',
        'R7P': 'Transit, cutaway (156 in wheelbase), 410L series',
        'R7Z': 'Transit, regular cab (156 in wheelbase), 410L series',
        'S4U': 'Transit, high roof line, RH side sliding load door, cargo van (148 in wheelbase), dual rear wheels, 470E series',
        'S4X': 'Transit, high roof line, RH side sliding load door, cargo van (148 in wheelbase), dual rear wheels, 470E series',
        'S6P': 'Transit, cutaway (138 in wheelbase), dual rear wheels, 470M series',
        'S6Z': 'Transit, regular cab (138 in wheelbase), dual rear wheels, 470M series',
        'S8P': 'Transit, cutaway (156 in wheelbase), dual rear wheels, 470L series',
        'S8Z': 'Transit, regular cab (156 in wheelbase), dual rear wheels, 470L series',
        'S9P': 'Transit, cutaway (178 in wheelbase), dual rear wheels, 470EL series',
        'S9Z': 'Transit, regular cab (178 in wheelbase), dual rear wheels, 470EL series',
        'U4X': 'Transit, wagon (178 in wheelbase), dual rear wheels',
        'W2C': 'Transit, medium roof line, RH side sliding load door, cargo van (148 in wheelbase), 430L series',
        'W2D': 'Transit, medium roof line, dual sliding load doors, cargo van (148 in wheelbase), 430L series',
        'W2U': 'Transit, high roof line, dual sliding load doors, cargo van (148 in wheelbase), 430L series',
        'W2X': 'Transit, high roof line, RH side sliding load door, cargo van (148 in wheelbase), 430L series',
        'W2Y': 'Transit, medium-low roof line, RH side sliding load door, cargo van (148 in wheelbase), 430L series',
        'W2Z': 'Transit, medium-low roof line, RH side swinging load doors, cargo van (148 in wheelbase), 430L series',
        'W3U': 'Transit, high roof line, dual sliding load doors, cargo van (148 in wheelbase), 430E series',
        'W3X': 'Transit, high roof line, RH side sliding load door, cargo van (148 in wheelbase) 430E series',
        'W7P': 'Transit, cutaway (156 in wheelbase), 430L series',
        'W7Z': 'Transit, regular cab (156 in wheelbase), 430L series',
        'X2C': 'Transit, medium roof line, RH side sliding load door, wagon (148 in wheelbase), 410L series',
        'X2X': 'Transit, medium-low roof line, RH side swinging load doors, wagon (148 in wheelbase), 410L series',
        'X2Y': 'Transit, medium-low roof line, RH side sliding load door, wagon (148 in wheelbase), 410L series',
        'X2Z': 'Transit, medium-low roof line, RH side swinging load doors, wagon (148 in wheelbase), 410L series'},
  'engine': {'G': '3.5L, gasoline turbocharged direct injection (GTDI), V6, gasoline',
            'M': '3.7L, 4-valve, direct acting mechanical buckets (DAMB), V6, gasoline',
            'V': '3.2L, DOHC , electronic fuel injection (EFI) in-line 5-cylinder diesel' },
  'year': {'F': '2015'},
  'plant': {'K': 'Kansas City Assembly (Claycomo, Missouri)'}
}


def decode(vin):
  wmi = lookup['wmi'][vin[0:3]]
  restraint = lookup['restraint'][vin[3]]
  body = lookup['body'][vin[4:7]]
  engine = lookup['engine'][vin[7]]
  year = lookup['year'][vin[9]]
  plant = lookup['plant'][vin[10]]
  serial = vin[11:17]

  return '\n'.join([wmi, restraint, body, engine, year, plant, serial])

print decode(vin)
