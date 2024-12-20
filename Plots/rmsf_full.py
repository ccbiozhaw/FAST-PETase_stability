import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set Seaborn style
sns.set_style("whitegrid")

# Define your data
data = {
    "WT-PETase": np.array([0.294367872, 0.238756618, 0.16124893, 0.095936842, 0.067185585, 0.094338928, 0.083753682, 0.047426031, 0.053365945, 0.037993225, 0.033236596, 0.044130455, 0.048659955, 0.049724006, 0.062686218, 0.048099879, 0.064272043, 0.044112211, 0.02566467, 0.036189555, 0.027379921, 0.029602909, 0.026708338, 0.027723651, 0.029372535, 0.037791701, 0.041836633, 0.03576464, 0.03125117, 0.035063299, 0.037702197, 0.029299969, 0.038552135, 0.042591475, 0.038974317, 0.046207953, 0.037152415, 0.032981988, 0.022485652, 0.018626949, 0.014866195, 0.017360839, 0.019261804, 0.01451733, 0.015012337, -0.012562975, 0.011354014, 0.020309392, 0.014932044, 0.012986949, 0.015620909, 0.019617821, 0.027174661, 0.03144321, 0.041559275, 0.051757702, 0.054508421, 0.054869936, 0.057128422, 0.065154608, 0.061688832, 0.051719081, 0.053117305, 0.054037729, 0.041942099, 0.043399049, 0.051893492, 0.03933771, 0.023007766, 0.025891996, 0.031866364, 0.025263765, 0.018220586, 0.022846688, 0.021036956, 0.016046259, 0.012743441, 0.011712045, 0.014921657, 0.020199772, 0.028345235, 0.036251213, 0.05182566, 0.046808969, 0.037616074, 0.051403609, 0.031053698, 0.045064474, 0.034337979, 0.071010316, 0.076471904, 0.080475019, 0.063736081, 0.057327099, 0.070496201, 0.06156096, 0.047540596, 0.04557235, 0.048040046, 0.042020567, 0.031734989, 0.030038482, 0.032750763, 0.027430539, 0.019935162, 0.022851286, 0.023728284, 0.018422939, 0.01579287, 0.019413998, 0.013852289, 0.027533086, 0.023211095, 0.022781561, 0.020767724, 0.015623912, 0.018575142, 0.016413011, 0.013676017, 0.013448731, 0.013382257, 0.012006719, 0.009002213, 0.012890707, 0.024956286, 0.03515247, 0.048100122, 0.047611811, 0.074105253, 0.054717027, 0.070859094, 0.069605327, 0.094216458, 0.128508807, 0.105871621, 0.122207051, 0.131390276, 0.101732776, 0.081073836, 0.08621524, 0.099666109, 0.104025577, 0.080857957, 0.039845636, 0.021420903, 0.006448833, 0.026044291, 0.04089803, 0.042136964, 0.043691147, 0.036572006, 0.04907213, 0.034958371, 0.061554985, 0.05885713, 0.082692501, 0.094539487, 0.124445103, 0.113854824, 0.16172869, 0.158446926, 0.097478658, 0.093740577, 0.083900549, 0.06767812, 0.050724329, 0.046177907, 0.026180369, 0.027853604, 0.016634935, 0.018375443, 0.016805591, 0.026730297, 0.035377355, -0.006545094, 0.003966959, 0.016317062, -0.017749009, -0.02550669, -0.005180236, 0.005269256, 0.012751782, 0.023349987, 0.021044622, 0.033187253, 0.018259327, 0.021041348, 0.036547671, 0.037888014, 0.024948456, 0.038899672, 0.057945335, 0.047055031, 0.045738384, 0.050250574, 0.036095454, 0.021879124, 0.020176399, 0.012992181, 0.012018841, 0.006013956, 0.012658838, 0.015129461, 0.002646292, -0.001157111, -0.001926947, 0.017253077, 0.037270118, 0.10184478, 0.067516702, 0.111912875, 0.131624795, 0.129608349, 0.147910602, 0.107386151, 0.097244624, 0.042833068, 0.049588355, 0.053740784, 0.03604833, 0.03446385, 0.032259217, 0.024016643, 0.017283868, 0.018493564, 0.019642408, 0.016390389, 0.013804651, 0.02213043, 0.025683957, 0.01750579, 0.021259089, 0.033870463, 0.04402269, 0.023918421, 0.027332038, 0.019665792, 0.034773554, 0.015252725, 0.009012912, 0.007189522, 0.013853222, 0.006713665, 0.005181893, 0.018502134, -0.011864895, -0.027626733, -0.030579537, -0.030229567, -0.038581836, -0.039694406, -0.053056851, -0.119038492, -0.051145172, -0.05517166, 0.012500036, 0.01584283, 0.02416918, 0.023839287, 0.020769235, 0.027841056, 0.069727183, 0.158035178]),
    "Std_WT-PETase": np.array([0.251510559, 0.232384508, 0.207896104, 0.130662745, 0.060312131, 0.08095581, 0.072834914, 0.063017196, 0.06287493, 0.061932713, 0.056722146, 0.063148967, 0.055572612, 0.055075436, 0.064744867, 0.040301027, 0.042856077, 0.028745363, 0.013940093, 0.018118374, 0.020118128, 0.020554831, 0.016013809, 0.014932107, 0.014251056, 0.013736088, 0.011209809, 0.012570774, 0.033648329, 0.028589181, 0.014971273, 0.01976933, 0.016855793, 0.015978949, 0.021703912, 0.015924042, 0.01047149, 0.009755011, 0.007101242, 0.010578978, 0.009147727, 0.012640407, 0.016019962, 0.02940316, 0.090510654, 0.086362265, 0.035444064, 0.013143456, 0.010606773, 0.007497573, 0.006793356, 0.005610153, 0.006456129, 0.006346808, 0.013310949, 0.01508204, 0.021742869, 0.032296847, 0.036160934, 0.021216476, 0.022097174, 0.021847898, 0.027876841, 0.030792441, 0.02509098, 0.028672592, 0.039890519, 0.029890421, 0.015162122, 0.016994293, 0.021711654, 0.019790026, 0.011941291, 0.015232162, 0.015011832, 0.010654454, 0.007324456, 0.006152666, 0.0055414, 0.003865474, 0.010249781, 0.014188548, 0.020716477, 0.027888817, 0.026781072, 0.036819856, 0.045467618, 0.048134524, 0.062528221, 0.032905857, 0.03161629, 0.02350733, 0.027671484, 0.02963406, 0.020397532, 0.015251962, 0.017994097, 0.012374154, 0.011249565, 0.011463599, 0.007789322, 0.009041431, 0.011844395, 0.008850595, 0.005306241, 0.007398017, 0.008373551, 0.007155893, 0.007210465, 0.009403211, 0.029581083, 0.010516524, 0.013419394, 0.004296584, 0.006271982, 0.009042159, 0.008281305, 0.014869678, 0.01222901, 0.008550366, 0.009060529, 0.013454025, 0.013263405, 0.01275708, 0.00997248, 0.013006137, 0.011146561, 0.018740959, 0.025201825, 0.016165675, 0.019109011, 0.019800683, 0.026359968, 0.058299567, 0.037610833, 0.036505993, 0.066224414, 0.046556675, 0.022777136, 0.028751105, 0.051699464, 0.032951514, 0.046584623, 0.032507094, 0.066538588, 0.062244423, 0.019839311, 0.016663518, 0.013237155, 0.008859976, 0.005574434, 0.015223141, 0.010044331, 0.024688998, 0.019315093, 0.06369624, 0.05817727, 0.075411147, 0.02580049, 0.048614824, 0.053641268, 0.048050326, 0.044393256, 0.025005565, 0.019606171, 0.016629546, 0.013891063, 0.009623556, 0.007041592, 0.005787569, 0.007674665, 0.010406112, 0.021307667, 0.036722432, 0.063728141, 0.076474168, 0.081036834, 0.124502047, 0.055971115, 0.053125251, 0.037985265, 0.034170676, 0.030830789, 0.030598841, 0.035118548, 0.024034173, 0.018794472, 0.021432636, 0.017330231, 0.012114629, 0.018722414, 0.020285881, 0.016097835, 0.016910978, 0.02070773, 0.012103237, 0.008479287, 0.007163429, 0.007133533, 0.008713314, 0.012922137, 0.01545105, 0.013638711, 0.029750151, 0.056346245, 0.063844123, 0.082562828, 0.114455419, 0.083449827, 0.0389191, 0.070341348, 0.070604753, 0.05324012, 0.06125397, 0.040751355, 0.032490797, 0.017508877, 0.018233725, 0.025234172, 0.024948374, 0.016375983, 0.016991372, 0.018720807, 0.014158528, 0.009820802, 0.00947004, 0.009548231, 0.007535704, 0.009363863, 0.007780354, 0.006856946, 0.007971749, 0.010760053, 0.02222749, 0.024840508, 0.023166763, 0.043221137, 0.039378082, 0.024305128, 0.035777882, 0.036457081, 0.018293367, 0.009175403, 0.010625895, 0.019366349, 0.025154478, 0.038209783, 0.064734282, 0.078281129, 0.098060819, 0.129906785, 0.117163613, 0.050043026, 0.029589841, 0.026729339, 0.012664386, 0.010064132, 0.01048156, 0.011402552, 0.006384308, 0.034436465, 0.124275468, 0.16360242]),
    "FAST-PETase": np.array([-0.365509573, -0.258366956, -0.197722222, -0.148071412, -0.01860174, -0.015240648, -0.013099994, -0.008680994, -0.011287795, -0.000610046, -0.010823458, 0.021947862, 0.025398364, -0.003312309, 0.009635576, 0.005437758, -0.011920458, -0.009015043, -0.0024599, -0.004507122, -0.005330932, -0.005705945, -0.004991077, -0.002753165, -0.002821242, -0.011499379, -0.011927559, -0.013415361, -0.01271774, -0.013691526, -0.014132596, -0.013249883, -0.017031976, -0.020759857, -0.026338794, -0.023879007, -0.014715248, -0.004636206, -0.00271642, -0.001626312, -0.002621124, -0.003500989, 0.000973564, 0.020816293, 0.080485318, 0.007363718, -0.008572157, -0.006617298, -0.005331528, -0.005650472, -0.00311213, -0.002698536, -0.00953864, -0.018185751, -0.033910682, -0.028674298, -0.042140516, -0.05148444, -0.094924301, -0.052755495, -0.049594473, -0.021583976, -0.017997816, -0.031972251, -0.012119091, -0.011715801, -0.01354796, -0.012872611, -0.002105818, -0.000170543, -0.005587033, -0.006454145, 0.000574276, -0.0031886, -0.000922231, -0.000169704, 0.000990479, 0.003482955, -0.00072116, -0.00427018, -0.010363605, -0.014244256, -0.027327479, -0.039926662, -0.049558798, -0.062286104, -0.092350013, -0.096324488, -0.081361828, -0.075270856, -0.066602186, -0.068538145, -0.059492635, -0.04494041, -0.040513533, -0.031205318, -0.026734567, -0.020559662, -0.014526738, -0.014493385, -0.008515429, -0.00143009, -0.005021345, -0.007065335, -0.003071478, -0.006507009, -0.010148135, -0.007762973, -0.008051703, -0.010410448, -0.010855191, -0.014068946, -0.011767092, -0.008850636, -0.007618487, -0.006213969, -0.008783916, -0.010240685, -0.005766747, -0.006634709, -0.01003982, -0.013666816, -0.006877236, -0.0037834, -0.01021214, -0.011023564, -0.011810689, -0.016120659, -0.016955735, 0.001631874, -0.015697284, -0.025124072, -0.02481939, -0.032948332, -0.03046334, -0.054805624, -0.043416757, -0.023843362, -0.045538164, -0.051522239, -0.036593704, -0.062126801, -0.0617178, -0.036290608, -0.036738427, -0.01969782, -0.012517831, -0.009387172, -0.009800528, -1.31978E-05, -0.000587803, 0.011778818, 0.007855797, -0.034057324, -0.027392463, -0.062126774, -0.077671187, -0.096873032, -0.090704519, -0.083451457, -0.080180317, -0.05917469, -0.073282328, -0.045630968, -0.037680353, -0.061232006, -0.010185725, -0.000748362, -1.32594E-05, -0.003709935, -0.001453353, -0.00708577, -0.010249011, -0.003024679, -0.012012476, 0.014924734, 0.026551117, 0.065103914, 0.008203696, -0.004519165, -0.018515342, -0.026254863, -0.036033055, -0.028482715, -0.066403318, -0.032290418, -0.029000127, -0.041062016, -0.03976838, -0.017008806, -0.0192155, -0.030846608, -0.030873999, -0.050618162, -0.03433294, -0.021035057, -0.001460329, -0.000214063, 0.000146038, -0.004444679, -0.010396483, -0.015450588, -0.013728219, -0.010648347, -0.00144317, 0.060146262, 0.074141725, 0.057139584, 0.007471072, 0.021436205, 0.04554795, 0.08028824, 0.08454273, 0.091749426, 0.06574914, 0.038427428, 0.009029598, 0.020353992, 0.009918937, 0.008175615, 0.004375487, 0.004025372, 0.008807681, 0.010781997, 0.012835327, -0.002900979, -0.005269441, -0.00079622, 8.20094E-05, -0.005478114, -0.005481021, 0.000168775, -0.009053972, -0.026516965, -0.015378051, -0.014387885, -0.012196001, -0.004890117, -0.003775066, -0.007121614, -0.009932212, -0.00488317, -0.003537237, -1.77738E-05, -0.005636231, -0.009154875, -0.002215237, -0.011445886, -0.010822267, -0.006276684, -0.007792854, -0.009929017, -0.014035473, -0.014492496, -0.010896984, -0.006404697, -0.000271748, -0.005242305, -0.002828949, -0.003237312, -0.018777292, -0.032613212, -0.070748813]),
    "Std_FAST-PETase": np.array([0.35818381, 0.300358974, 0.260488624, 0.222222265, 0.17019351, 0.157315132, 0.119741532, 0.062616453, 0.042932138, 0.044409458, 0.051140618, 0.048262243, 0.037671394, 0.045440177, 0.043795617, 0.03453874, 0.067430462, 0.031951788, 0.018090622, 0.023534419, 0.018671739, 0.019511444, 0.015241393, 0.014312579, 0.011410336, 0.015792208, 0.013735615, 0.012751135, 0.013828776, 0.011086591, 0.008412013, 0.010856033, 0.012406999, 0.008611568, 0.017160809, 0.020273111, 0.018648728, 0.009958425, 0.006648211, 0.00824532, 0.00938009, 0.013156591, 0.019006375, 0.040806072, 0.093624375, 0.066543791, 0.021753042, 0.013103033, 0.011982452, 0.008436124, 0.005961292, 0.005524297, 0.004079791, 0.005842268, 0.006892936, 0.026108177, 0.062492216, 0.108967114, 0.084700379, 0.058633007, 0.03680684, 0.021769711, 0.023968837, 0.041701692, 0.027024371, 0.02804232, 0.033675032, 0.022751343, 0.013226676, 0.016312786, 0.017742305, 0.015756396, 0.014440333, 0.018842687, 0.018554764, 0.018109948, 0.011702903, 0.00878502, 0.006249289, 0.004268712, 0.008517414, 0.010462469, 0.013262239, 0.017959591, 0.029495575, 0.030948036, 0.031748252, 0.039326784, 0.032294055, 0.039731809, 0.037622551, 0.026202272, 0.02999306, 0.025537187, 0.026464362, 0.017433985, 0.015444324, 0.014443887, 0.008418188, 0.007829782, 0.005937914, 0.004951517, 0.005235579, 0.004388649, 0.003836533, 0.006503468, 0.007330851, 0.006349206, 0.008347196, 0.010914166, 0.0086952, 0.011483749, 0.008827009, 0.008166778, 0.006989068, 0.009641871, 0.010395017, 0.011500098, 0.00994336, 0.009014359, 0.010286073, 0.020422439, 0.013838002, 0.008842077, 0.005415454, 0.008199839, 0.008739446, 0.012531295, 0.017197728, 0.021518064, 0.030171882, 0.040292966, 0.038147238, 0.037498397, 0.035997874, 0.060472462, 0.039713573, 0.024993131, 0.042665283, 0.043037235, 0.032253749, 0.04454496, 0.034775382, 0.025626135, 0.022871741, 0.018775736, 0.005055055, 0.005821698, 0.011694862, 0.016489731, 0.01248096, 0.018340125, 0.018105096, 0.027052337, 0.03912235, 0.061408412, 0.083481408, 0.101656114, 0.057526303, 0.031855576, 0.047285311, 0.028318396, 0.034209176, 0.02631163, 0.01977266, 0.012542094, 0.012563701, 0.007829351, 0.008532893, 0.017607009, 0.02232225, 0.023012212, 0.030102039, 0.021020019, 0.05363748, 0.051202428, 0.048849406, 0.085819341, 0.070958928, 0.04690345, 0.03689437, 0.029413365, 0.036279146, 0.042620924, 0.053462526, 0.020839794, 0.011546275, 0.013153098, 0.015461869, 0.010453882, 0.006083039, 0.012717805, 0.013939596, 0.023316382, 0.016667305, 0.012751168, 0.013374887, 0.008326582, 0.009309009, 0.011040993, 0.011079467, 0.013764569, 0.016115673, 0.024788922, 0.052340277, 0.053045745, 0.096636828, 0.133935508, 0.059031326, 0.039773244, 0.070554503, 0.084002719, 0.098938894, 0.089027731, 0.075238, 0.043332957, 0.030592453, 0.034421524, 0.031441713, 0.021046888, 0.021174161, 0.027305617, 0.023219922, 0.016547734, 0.021236029, 0.018890394, 0.011603797, 0.008472415, 0.01132494, 0.011337254, 0.008688933, 0.006276878, 0.007719266, 0.040714452, 0.024629566, 0.025321069, 0.025115503, 0.025482392, 0.015296378, 0.016984087, 0.020312875, 0.014957997, 0.010477227, 0.011420374, 0.019453733, 0.017235756, 0.022032282, 0.024986665, 0.017812276, 0.022391848, 0.022894479, 0.015585501, 0.013641919, 0.009285601, 0.006609309, 0.007945663, 0.009614883, 0.010507487, 0.012321174, 0.013229168, 0.044582341, 0.099491916, 0.163093059]),
}


# Define x-axis values
start_residue = 30
end_residue = 292
x = np.arange(start_residue, end_residue + 1)

# Define colors
line_colors = ['#1E90FF', '#1E90FF', '#FF4500', '#FF4500']
shade_colors = ['#1E90FF', '#FF4500']

# Define figure size in cm and convert to inches
width_cm = 16
height_cm = 10
width_inch = width_cm / 2.54
height_inch = height_cm / 2.54

# Update plot settings
plt.rcParams.update({'font.family': 'Arial'})

# Create the plot
plt.figure(figsize=(width_inch, height_inch))

# Plot RMSF and shade standard deviations
shade_color_index = 0
for i, (key, values) in enumerate(data.items()):
    if "Std" not in key:
        plt.plot(x, values, label=key, color=line_colors[i])
    else:
        mean_key = key.replace("Std_", "")
        std = values
        mean = data[mean_key]
        if shade_color_index == 0:
            plt.fill_between(x, mean - std, mean + std, alpha=0.3, color=shade_colors[shade_color_index], zorder=1)
        else:
            plt.fill_between(x, mean - std, mean + std, alpha=0.3, color=shade_colors[shade_color_index], zorder=1)
        shade_color_index = (shade_color_index + 1) % len(shade_colors)  # Cycle through colors

# Customize plot
plt.xlabel("Residue Numbering", fontsize=10, labelpad=70)
plt.ylabel("ΔRMSF mean(50°C)-mean(30°C)", fontsize=10)
plt.legend(fontsize=8, loc='best', frameon=False)
axes = plt.gca()
axes.xaxis.grid()
plt.tick_params(axis='x', bottom=False, rotation=90, size=7)  # Disable x-axis ticks
plt.xlim(start_residue, end_residue)
plt.ylim(-0.8, 0.8)

# Show residue numbers below x-axis (every 8th residue)
plt.xticks(x[::8], [int(residue) for residue in x[::8]])
axes.spines['bottom'].set_position(('data', -0.2))
plt.gca().yaxis.set_ticks_position('none')  # Disable y-axis ticks

plt.text(152, 0.45, "S121E", fontsize=8, horizontalalignment='center', verticalalignment='center', color='dimgrey' , bbox=dict(facecolor='white', edgecolor='dimgrey', boxstyle='round,pad=0.5'))
plt.plot([134, 152], [0.45, 0.45], color='dimgrey', linestyle='--')
plt.plot([121, 134], [0, 0.45], color='dimgrey', linestyle='--')

plt.text(225, 0.45, "D186H", fontsize=8, horizontalalignment='center', verticalalignment='center', color='dimgrey' , bbox=dict(facecolor='white', edgecolor='dimgrey', boxstyle='round,pad=0.5'))
plt.plot([214, 225], [0.45, 0.45], color='dimgrey', linestyle='--')
plt.plot([186, 214], [0, 0.45], color='dimgrey', linestyle='--')

plt.text(206, -0.47, "R224Q", fontsize=8, horizontalalignment='center', verticalalignment='center', color='dimgrey' , bbox=dict(facecolor='white', edgecolor='dimgrey', boxstyle='round,pad=0.5'))
plt.plot([225, 206], [-0.47, -0.47], color='dimgrey', linestyle='--')
plt.plot([225, 225], [0, -0.47], color='dimgrey', linestyle='--')

plt.text(216, -0.6, "N233K", fontsize=8, horizontalalignment='center', verticalalignment='center', color='dimgrey' , bbox=dict(facecolor='white', edgecolor='dimgrey', boxstyle='round,pad=0.5'))
plt.plot([233, 216], [-0.6, -0.6], color='dimgrey', linestyle='--')
plt.plot([233, 233], [0, -0.6], color='dimgrey', linestyle='--')

plt.text(262, -0.50, "R280A", fontsize=8, horizontalalignment='center', verticalalignment='center', color='dimgrey' , bbox=dict(facecolor='white', edgecolor='dimgrey', boxstyle='round,pad=0.5'))
plt.plot([281, 262], [-0.50, -0.50], color='dimgrey', linestyle='--')
plt.plot([281, 281], [0, -0.50], color='dimgrey', linestyle='--')

residue_ranges = [(54, 70),(82, 100), (108, 134), (152, 176), (182, 198), (210, 226), (233, 247)]

# Draw grey boxes for specified residue ranges
for range_start, range_end in residue_ranges:
    plt.axhspan(-0.2, 0.2, xmin=(range_start - start_residue) / (end_residue - start_residue), xmax=(range_end - start_residue) / (end_residue - start_residue), color='lightgrey', alpha=0.5)
    plt.text((range_end + range_start) / 2, 0.25, f'IS{residue_ranges.index((range_start, range_end)) + 1}', horizontalalignment='center', fontsize=8, color='grey', fontweight='semibold')  # Position the text above the box


# Show plot
plt.tight_layout()
plt.savefig("rmsf_full.png", dpi=5000)
plt.show()



