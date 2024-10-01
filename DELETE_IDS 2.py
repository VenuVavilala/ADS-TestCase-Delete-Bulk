import requests
import base64

# Create ads personal access token - full access
# Run with `python DELETE_IDS.py`

delete_ids = [35916, 35917, 35919, 35920, 35921, 35922, 35923, 35924, 35925, 35926, 35927, 35928, 35929, 35930, 35931, 35932, 35933, 35934, 35935, 35936, 35937, 35938, 35939, 35940, 35941, 35942, 35943, 35944, 35945, 35946, 35947, 35948, 35949, 35950, 35951, 35952, 35953, 35954, 35956, 35957, 35958, 35959, 35960, 35961, 35962, 35963, 35964, 35965, 35966, 35967, 35968, 35969, 35970, 35971, 35972, 35973, 35974, 35975, 35976, 35977, 35978, 35986, 35987, 35988, 35989, 35990, 35991, 35992, 35993, 35994, 35995, 35996, 35997, 35998, 35999, 36000, 36007, 36040, 36041, 36042, 36043, 36044, 36045, 36046, 36047, 36048, 36049, 36050, 36051, 36052, 36053, 36054, 36055, 36056, 36057, 36058, 36059, 36060, 36061, 36062, 36063, 36064, 36065, 36066, 36067, 36068, 36069, 36070, 36071, 36072, 36073, 36074, 36076, 36077, 36078, 36079, 36080, 36081, 36082, 36083, 36084, 36085, 36086, 36087, 36088, 36089, 36090, 36091, 36092, 36093, 36094, 36095, 36096, 36097, 36099, 36100, 154459, 154465, 154466, 154467, 154468, 154469, 154470, 154471, 154472, 154473, 154474, 154475, 154476, 154477, 154478, 154479, 154480, 154481, 154482, 154483, 154484, 154485, 154486, 154487, 154488, 154489, 154490, 154491, 154492, 154493, 154494, 154495, 154496, 154497, 154498, 154499, 154500, 154501, 154502, 154503, 154504, 154505, 154506, 154507, 154508, 154509, 154510, 154511, 154512, 154513, 154514, 154515, 154516, 154517, 154518, 154519, 154520, 154521, 154522, 154523, 154528, 154529, 154530, 154531, 164529, 164538, 164539, 164557, 164558, 164562, 164585, 164586, 164598, 164599, 164600, 164601, 164618, 164622, 164623, 164631, 164701, 164702, 164704, 164705, 164707, 164710, 164712, 164717, 164718, 164720, 164721, 164730, 164731, 164742, 164750, 164751, 164752, 164754, 164755, 164756, 164757, 164758, 164759, 164760, 164768, 164769, 164770, 164772, 164778, 164784, 164785, 164787, 164790, 164792, 164797, 164798, 164808, 164814, 164815, 164817, 164818, 164819, 164820, 164821, 164836, 164845, 164846, 164864, 164865, 164869, 164874, 164875, 164897, 164899, 164921, 164922, 164923, 164924, 164925, 164926, 164954, 164970, 164973, 164974, 164975, 164976, 164977, 164986, 165038, 165039, 165046, 165047, 165048, 165049, 165058, 165062, 165063, 165064, 165065, 165069, 165071, 165072, 165074, 165075, 165076, 165077, 165078, 165084, 165099, 165100, 165101, 165104, 165105, 165107, 165110, 165111, 165113, 165127, 165128, 165140, 165143, 165179, 165196, 165211, 165213, 165234, 165235, 165236, 165237, 165238, 165240, 165241, 165248, 165249, 165254, 165270, 165271, 165273, 165274, 165275, 165276, 165282, 165286, 165288, 165289, 165291, 165300, 165301, 165318, 165340, 165341, 165342, 165388, 165389, 165390, 165391, 165411, 165412, 165413, 165513, 165514, 165515, 165642, 165656, 165657, 165673, 165691, 165705, 165706, 165767, 165930, 165931, 166011, 166012, 166017, 166068, 166070, 166071, 166072, 166111, 166141, 166142, 166143, 166144, 166145, 166157, 166158, 166165, 166166, 166168, 166169, 166170, 166171, 166173, 166183, 166184, 166185, 166186, 166200, 166226, 166228, 166229, 166238, 166239, 154532, 154533, 154534, 154535, 154536, 154537, 154538, 154539, 154540, 154541, 154542, 154543, 154544, 154545, 154546, 154547, 154549, 154550, 154551, 154552, 154554, 154555, 154556, 154557, 154558, 154559, 154560, 154561, 154562, 154563, 154564, 154565, 154566, 154567, 154568, 154569, 154570, 154571, 154572, 154573, 154574, 154575, 154576, 154577, 154578, 154579, 154580, 154581, 154582, 154583, 154584, 154585, 154586, 154587, 154588, 154589, 154590, 154591, 154592, 154593, 154594, 154595, 154596, 154597, 154598, 154599, 154600, 154601, 154602, 154603, 154604, 154605, 154606, 154607, 154608, 154609, 154610, 154611, 154612, 154613, 154614, 154615, 154616, 154617, 154618, 154619, 154620, 154621, 154622, 154623, 154624, 154625, 154626, 154627, 154628, 154629, 154630, 154631, 154632, 154633, 154634, 154635, 154636, 154637, 154638, 154639, 154640, 154641, 154642, 154643, 154644, 154645, 154646, 154647, 154648, 154649, 154650, 154651, 154652, 154653, 154654, 154655, 154686, 154687, 154693, 154694, 162278, 162284, 162285, 162286, 162287, 162288, 162289, 162290, 162291, 162292, 162341, 162600, 162605, 162606, 162607, 162610, 162611, 162612, 162624, 162639, 162648, 162649, 162669, 162683, 162701, 162726, 162727, 162728, 162729, 162733, 162734, 162735, 162736, 162753, 162760, 162761, 162769, 162799, 162800, 162801, 162802, 162803, 162804, 162813, 162821, 162822, 162823, 162831, 162832, 162835, 162876, 164458, 164459, 164460, 164469, 164470, 164471, 164472, 164475, 164476, 164477, 164487, 164488, 164489, 164490, 164493, 164494, 164498, 164499, 164500, 164501, 164502, 164506, 164507, 166240, 166273, 166284, 166315, 166316, 166326, 166327, 166328, 166329, 166332, 166362, 166363, 166373, 166374, 166397, 166398, 166403, 166404, 166405, 166406, 166409, 166410, 166411, 166412, 166466, 166468, 166546, 166547, 166567, 166568, 166569, 166570, 166571, 166574, 166575, 166581, 166596, 166597, 166598, 166599, 166600, 166601, 166602, 166603, 166604, 166605, 166606, 166607, 166608, 166609, 166610, 166612, 166613, 166614, 166615, 166616, 166617, 166638, 166639, 166656, 166658, 166663, 166672, 166675, 166681, 166682, 166683, 166690, 166691, 166699, 166700, 166748, 166749, 166751, 166752, 166753, 166754, 166755, 166756, 166757, 166758, 166759, 166760, 166771, 166773, 166776, 166777, 166778, 166793, 166794, 166796, 166799, 166800, 166801, 166802, 166804, 166805, 166806, 166807, 166808, 166809, 166810, 166812, 166813, 166816, 166817, 166819, 166820, 166821, 166827, 166828, 166829, 166895, 166896, 166898, 166899, 166900, 166901, 166902, 166903, 166904, 166905, 166909, 166915, 166916, 166924, 166928, 166929, 166933, 166962, 166992, 166993, 166994, 166995, 166996, 166997, 166998, 166999, 167006, 167007, 167008, 167046, 167077, 167083, 167089, 167091, 168000, 168001, 168002, 168004, 168005, 168006, 168007, 168008, 168020, 168021, 168022, 168023, 168024, 168025, 168026, 168027, 168028, 168030, 168031, 168032, 168033, 168034, 168035, 168036, 168037, 168038, 168039, 168511, 168536, 168537, 168538, 168782, 169041, 169235, 169236, 169284, 169285, 169286, 169287, 169288, 169289, 169290, 169291, 169292, 169293, 169297, 169298, 169299, 169300, 169301, 169320, 169322,]


def deleteId(id):
    pat = 'XXXX'  # Your personal access token (PAT) here

    authorization = str(base64.b64encode(bytes(':'+pat, 'ascii')), 'ascii')
    
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Basic '+authorization
    }
    
    # Construct the URL dynamically using the current ID
    url = "https://dev.azure.com/XXX/ADS/_apis/test/testcases/{id}?api-version=7.1-preview.1"
    
    response = requests.delete(url, headers=headers)
    
    print(f"Deleted ID {id}: {response.text}")


for id in delete_ids:
    deleteId(id)


