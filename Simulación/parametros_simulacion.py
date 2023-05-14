from random import seed, randint
DIAS_DE_SIMULACION = 500
DIAS_TRANCIENTE = 150
MUESTRAS_POR_SIMULACION = 100

COSTO_VIDA = 6266

SIMULACIONES_POR_ESTRATEGIA = 3

NUMERO_SIMULACIONES_PARALELAS = 8

JORNADAS_POR_DIAS = 2

NUMERO_HOSPITALES = 1

SEED = 6942

seed(SEED)
ID_DIAS_MUESTRAS = [randint(DIAS_TRANCIENTE, DIAS_DE_SIMULACION - 1) for i in range(MUESTRAS_POR_SIMULACION)]

# ALGUNOS PARAMETROS QUE ESTÁN INCLUIDOS EN LA HOJA DE MATÍAS. ALGUNO PODRÍA SER ÚTIL PARA UN FUTURO
PERIODOS_RELEVANTES = 40 
PONDERADOR_ESPERAS = 1
CAPACIDAD_MAXIMA_LISTA_ESPERA = 2000
ANCHO_VENTANA_TEMPORAL_EN_HORAS = 12
TIEMPO_ESPERADO_MAXIMO = {1: 0,
                          2: 0,
                          3: 0,
                          4: 0,
                          5: 27,
                          6: 26,
                          7: 26,
                          8: 26.5,}


#PARAMETROS_ESTRATEGIA_PROVISORIOS = {1: {'H_1': {'ED': [{1: 86.7302830572678, 2: -26.378735486033246, 3: -40.25089887129645, 4: 24.514698187766253, 5: -21.761533936755097, 6: -3.9274215920870716, 7: -15.9724498714737, 8: -57.26267074851857}, {1: -61.54169712194785, 2: 32.3017343154998, 3: -44.643276888471654, 4: 21.761926735217664, 5: -36.10666292889957, 6: -5.6276622636805005, 7: 7.591354867101131, 8: -24.769942757410675}, -10.340330423750643], 'OR': [{1: 138.40675466135428, 2: 37.742635316240374, 3: -28.50349759322852, 4: 10.186014231246759, 5: -20.107389426349144, 6: 0.6830858068351926, 7: -25.889457504296033, 8: -12.492293473342624}, {1: -15.756434791862523, 2: -53.51870322598972, 3: 11.354586974932431, 4: 0.52024756478618, 5: -22.385604785992527, 6: -20.551230010392207, 7: -2.746367130867018, 8: 5.556179162891677}, -53.42445087970485], 'ICU': [{1: 159.0421252684709, 2: -5.660949048052069, 3: -29.49926281029302, 4: -31.79940083581581, 5: -11.823616230004305, 6: -52.821662213143064, 7: -22.08163101166841, 8: -19.322926560648355}, {1: -27.471445770948044, 2: 2.1394596096095064, 3: -10.256956666903681, 4: -25.565934806532706, 5: -27.52221828708509, 6: 16.541983265789927, 7: -32.186098233872954, 8: -34.993279533718734}, -53.69048645610573], 'SDU_WARD': [{1: 180.63750416835126, 2: 29.35110011851395, 3: -11.606538653141094, 4: 15.737041806916208, 5: -47.68151753173572, 6: 7.611851139397519, 7: -2.5304193664625423, 8: -15.361994074569854}, {1: -15.227941684377765, 2: -27.49640630550911, 3: 31.351575749522937, 4: -34.75191109612376, 5: 17.04620613656809, 6: -25.956380705632647, 7: 9.817869709208463, 8: -26.04115229500307}, 63.835643656461436], 'GA': [{1: -37.522111425695314, 2: -10.874205059948547, 3: -9.696207875047289, 4: -22.479386815213804, 5: -41.41531300450404, 6: -28.39919850780467, 7: -13.479867224478353, 8: -70.55706015535787}, {1: -17.41191480040781, 2: -24.717568223322257, 3: 22.21442705018201, 4: -8.299819711840419, 5: -18.162620758706858, 6: 4.813577757944543, 7: -1.7646383976052533, 8: -46.686358209501606}, -50.378774437339004]}, 'WL': {'WL': [{1: -3.956484982430141, 2: 12.348631067187547, 3: -4.568864816792477, 4: -55.9414387232575, 5: -7.608679946037393, 6: -4.813299508559304, 7: -21.866369702068265, 8: -59.58769543266965}, {1: 0.9488259125677789, 2: -50.32641411503378, 3: -14.142309908228972, 4: -21.5156709400213, 5: 2.1442285460564996, 6: -13.685909933738731, 7: -55.21790040001429, 8: -18.457887407339463}, -35.46962029856547]}}, 2: {'H_1': {'ED': [{1: -29.74499511978494, 2: -36.533846817678196, 3: 17.58979488809389, 4: -37.50856627806746, 5: -11.177174079349815, 6: 3.9572639725951007, 7: -19.137188382062913, 8: 15.574912783069449}, {1: -2.017466813612268, 2: 13.790047957463289, 3: -15.85521579095164, 4: -34.14237494699946, 5: -0.40227070552619004, 6: 10.784835863899533, 7: 1.000715553000255, 8: 4.687040114331616}, -34.79161107823416], 'OR': [{1: -13.82931732436477, 2: -1.2432068005341677, 3: -10.974297860965237, 4: -12.409745850714163, 5: -21.518696178089495, 6: -36.245681493067025, 7: -22.781466885979555, 8: -44.55977858400955}, {1: 10.766405576590463, 2: 17.72934478948924, 3: -0.34891565737790486, 4: 6.171242576198974, 5: 10.433340770078829, 6: -36.52280156467939, 7: -20.4130394730203, 8: -4.508261166350113}, -13.58867917302656], 'ICU': [{1: 0.24076541641234606, 2: -34.54875891256322, 3: -41.844851582497235, 4: -2.500579661015271, 5: 12.686897716859631, 6: -31.831077083432344, 7: 6.190153823592791, 8: 3.093795719516198}, {1: 0.9999558913444986, 2: -31.220581424150623, 3: 1.712741319030977, 4: -27.549201580472108, 5: -22.97592574174596, 6: -43.92226468692467, 7: -39.017483795478135, 8: -34.502869650842676}, -39.65720707326718], 'SDU_WARD': [{1: -29.39101429361812, 2: 8.826064624022234, 3: -9.102623690638808, 4: -15.428416768665487, 5: -19.59460876032837, 6: -0.18680073631226612, 7: -10.333046327724507, 8: 6.805755141167438}, {1: 22.27318639408006, 2: -29.010636325179313, 3: -4.444484345854235, 4: -24.56993787909248, 5: 13.165603117401744, 6: -1.254388313546464, 7: -4.795402767921683, 8: -32.354702956735125}, 83.9518290638926], 'GA': [{1: -24.0551328888279, 2: 23.681102766215822, 3: -19.02595488655248, 4: -18.318116953301836, 5: -47.936408492775115, 6: -53.19763485344348, 7: 13.043328890968862, 8: -21.058067697170795}, {1: 21.094349658233888, 2: -23.50448787606657, 3: -10.192698800861777, 4: -6.451784822454446, 5: -31.33947339972941, 6: -2.706737634386311, 7: -42.41311573078521, 8: -18.802664681137806}, -36.7907247035467]}, 'WL': {'WL': [{1: -19.489380340332975, 2: -24.867871272614316, 3: -2.465661549592644, 4: -5.532952870812098, 5: -29.411599205872573, 6: -20.143652295438834, 7: -3.7830265010016717, 8: -29.618203717430642}, {1: 37.48767119872637, 2: -11.037241239816174, 3: -4.337817707031899, 4: -15.26331881905498, 5: -29.45883518452826, 6: -15.038674579961853, 7: -54.40923540527639, 8: -24.161316663810506}, -32.784693962766866]}}, 3: {'H_1': {'ED': [{1: -75.28355405210866, 2: -37.0533232539629, 3: 27.601109751597097, 4: -61.49250563505875, 5: -3.9411530699741704, 6: -73.98204896637118, 7: -6.599129104248178, 8: -103.58355390548869}, {1: -30.870619188528458, 2: -19.525492060883057, 3: -43.119640946891764, 4: -15.711224117388175, 5: -33.54604141993529, 6: -9.569327511631803, 7: -6.155064408729821, 8: -32.15360088615013}, 63.35246353713704], 'OR': [{1: -69.04008038772974, 2: -37.11710471259897, 3: -64.11344954161903, 4: -50.259064158416805, 5: -15.84960830675315, 6: -32.50311659875775, 7: -49.84543302849693, 8: -42.14079885981937}, {1: -29.419952965693014, 2: -21.222664013713203, 3: -5.6098695633681, 4: -3.846864557179442, 5: -0.9357092441348343, 6: -45.86779629562699, 7: -44.86472063791364, 8: -67.07816309360052}, -94.6738731651086], 'ICU': [{1: -7.552454327589173, 2: -24.875289083808678, 3: -50.729096078001525, 4: -21.936549987455233, 5: -29.220408043745454, 6: -20.728495658555147, 7: -34.14742795135739, 8: -48.260490916401075}, {1: -62.377761488406065, 2: -21.065264812028612, 3: -53.750482080914864, 4: -53.345533519060055, 5: -74.08652331752238, 6: -80.47873699608778, 7: -64.90635209801856, 8: -10.62314639322343}, -43.2958939821939], 'SDU_WARD': [{1: -67.70014442343648, 2: -37.64788100360839, 3: 11.136485197680418, 4: -44.48406636508139, 5: -9.135936800932933, 6: -0.24465599378506298, 7: -40.8239262876233, 8: -23.20375472976415}, {1: -9.524563380950053, 2: -26.096181212902668, 3: -27.216526866904868, 4: -48.10178277917777, 5: -33.41699008942132, 6: -15.633349217326444, 7: -16.252749449210015, 8: -65.45774564838466}, -16.213473876311262], 'GA': [{1: -42.926314199678906, 2: -34.86840937565522, 3: -22.40197261645457, 4: -39.529401910618176, 5: -38.78760149769982, 6: -44.9613711660762, 7: -14.679276635686078, 8: -35.04739764580027}, {1: -8.765484907456049, 2: -47.63745841048204, 3: -18.398078449628933, 4: -52.58729269100505, 5: -40.93175540864864, 6: -76.23523674715122, 7: -37.605685939153574, 8: -40.29908828151369}, -24.77584687203208]}, 'WL': {'WL': [{1: -42.01189624814042, 2: -17.164224114755758, 3: 7.586276822412671, 4: 27.97310080752959, 5: -103.83247751766054, 6: -14.184590444459362, 7: 57.47336133814034, 8: -13.108513993281308}, {1: 3.0111029652850227, 2: -35.55148120945647, 3: -87.73960621315034, 4: -11.74084779429386, 5: -76.49889811608209, 6: -58.86762913811121, 7: -24.858531383296686, 8: -22.287158421197248}, -11.51096092686607]}}, 4: {'H_1': {'ED': [{1: -3.641539086358126, 2: -3.9345630601964405, 3: -25.710616710232998, 4: 0.9328335668998946, 5: 1.7114270509438523, 6: -22.426744491375693, 7: -31.309831028707315, 8: -38.61862855524316}, {1: -31.222471244075905, 2: -0.6182531455250704, 3: -19.298865834975956, 4: -24.442031590632233, 5: -30.44578309582974, 6: 22.343306435742143, 7: 5.496563241378372, 8: -14.30306601563028}, -4.222748031998641], 'OR': [{1: -29.19804805981815, 2: -38.56415900388235, 3: -35.094543246616425, 4: -35.504045150264545, 5: -30.90951139780283, 6: -29.93871074346235, 7: -28.73702746532132, 8: -56.56768692052131}, {1: -14.990136956798787, 2: -26.370235298613387, 3: -31.07327696168288, 4: -20.846507718388764, 5: -19.00161174992589, 6: -10.17188022290995, 7: 0.17914212723833067, 8: 11.480901992291894}, -2.924975870318045], 'ICU': [{1: -24.6448134436866, 2: -32.33280732241895, 3: -55.92891457357631, 4: -59.28396884725721, 5: -11.783663739409187, 6: -30.163396682478858, 7: -10.02502384175151, 8: -6.377766129333235}, {1: -16.460639825339683, 2: -40.30057345973114, 3: -27.819660409248822, 4: -12.279591113115323, 5: -11.990413474395819, 6: -23.862930870440014, 7: -4.859246360215245, 8: -8.596570670935705}, -44.65752104488762], 'SDU_WARD': [{1: 14.647541708289033, 2: -13.865029858283656, 3: -1.2037590250827037, 4: -45.350650051720834, 5: -32.6317306081015, 6: -38.095001257557065, 7: 9.751026075719391, 8: -2.374082842497643}, {1: -25.192309819211854, 2: -20.81772779258455, 3: 17.863048447237727, 4: -30.511074299654183, 5: 4.993048633446303, 6: -4.053350436272481, 7: -41.88434469501529, 8: -31.01640055103121}, 61.15324246492268], 'GA': [{1: -27.745874441480744, 2: -4.339384004720932, 3: -13.064928255474177, 4: -2.1580953480416945, 5: -21.415755375556344, 6: -45.01143759104564, 7: -19.69438645980493, 8: -1.8071622495414168}, {1: 10.289799100429121, 2: -7.69479897736106, 3: -2.4379751610752294, 4: 5.032089770397318, 5: -20.25938321272345, 6: -10.19172162023278, 7: -14.01527467096747, 8: -28.89253003352529}, -56.15810650960371]}, 'WL': {'WL': [{1: 10.654125311368094, 2: -15.306629819132112, 3: 8.194055825684913, 4: -11.83783717695708, 5: 5.919677062588383, 6: 16.35978996168768, 7: -23.699107478547443, 8: -8.760963426454117}, {1: -6.714085223094138, 2: -7.422169547394808, 3: -17.89973360311159, 4: -25.30647324429641, 5: -39.398414042514645, 6: -29.606678743780446, 7: -9.399651395743993, 8: -28.438843822643566}, -24.016591979178042]}}, 5: {'H_1': {'ED': [{1: 23.338673513745533, 2: -1.4239323010943465, 3: -10.46245837861441, 4: -21.821834207746925, 5: -27.85492834479779, 6: -32.35826990162737, 7: -57.14465541930801, 8: -70.08799569018058}, {1: -22.64914483710484, 2: -51.24696754869262, 3: -26.83797281806672, 4: 20.41190660626206, 5: -33.244552856445424, 6: -53.55773566633857, 7: -26.191090563402913, 8: -39.674098343078}, -20.265432118833058], 'OR': [{1: -44.762020277371874, 2: -28.672784058896355, 3: -75.03597069417862, 4: -49.54645835191744, 5: -9.005324327807543, 6: -72.18721159891368, 7: -26.781384705526687, 8: -39.6777265604005}, {1: -41.439376066094574, 2: -61.48020400438452, 3: 22.042700289520837, 4: -110.5907482291534, 5: -61.98596548536995, 6: -100.28327128740335, 7: -47.66268354636706, 8: -43.71032538301833}, -52.26871354005422], 'ICU': [{1: -78.83560730872868, 2: -13.242322324980627, 3: -30.86361191227896, 4: 1.133843929390359, 5: -30.55849773971334, 6: -74.57727618157226, 7: -61.32623411501406, 8: -62.284145624811124}, {1: -10.766507640620027, 2: -67.45549219029223, 3: -66.17726770004982, 4: -40.54655932168465, 5: -8.537603092301689, 6: -62.90470465663989, 7: -52.98873615314665, 8: -37.63953071353338}, -14.89684107337885], 'SDU_WARD': [{1: 30.27430930947473, 2: -39.83217688956389, 3: -57.33271829344246, 4: -40.42991882042229, 5: -38.99194649571926, 6: -65.55854225473658, 7: -16.897916356078202, 8: -67.6842347694941}, {1: -42.92146841407703, 2: -2.6226906747935335, 3: -15.286251180345054, 4: -66.54034498600583, 5: -41.599127821258946, 6: 3.109229464129646, 7: 10.857503489376043, 8: -66.51163503119598}, 12.952594861932004], 'GA': [{1: -34.00736820051789, 2: -44.340288432482915, 3: -14.931682551619367, 4: -14.201387379114422, 5: -62.65476778463803, 6: -12.34661564213069, 7: -69.40213425343578, 8: -77.54939456681399}, {1: -48.83562638102839, 2: -101.13844349924925, 3: -49.16971608513232, 4: -30.97620022220844, 5: -18.91958375579376, 6: -47.00027518940079, 7: -32.319672031963336, 8: -61.61273250633915}, -75.04731767655423]}, 'WL': {'WL': [{1: -52.334793919162635, 2: -75.2336934946043, 3: -8.245419415658322, 4: -60.79314054618289, 5: -101.14669094118673, 6: -87.03162269422303, 7: -70.79376943589799, 8: -56.98681533052785}, {1: -39.16712281442024, 2: -82.00077075247114, 3: -64.24661212963282, 4: -129.4249623606855, 5: -39.7615524332008, 6: -48.68302447383533, 7: -51.62824347299633, 8: -38.13417097991726}, -56.475796210872545]}}, 6: {'H_1': {'ED': [{1: 2.080214740166948, 2: 16.72408574954052, 3: -0.5488654625144012, 4: 7.435133540336494, 5: -20.91859432184977, 6: -22.821971509467602, 7: -11.005092686329467, 8: -15.552214196686608}, {1: -6.231754275667953, 2: 7.283524591788147, 3: -35.16356513950657, 4: -22.13589168627032, 5: -13.087553748062081, 6: 0.524293940167329, 7: -9.524515939783427, 8: -17.949442110055188}, 30.61175793401121], 'OR': [{1: -23.32029552745665, 2: -12.93787800786569, 3: -1.913725302561339, 4: -2.7513205508649197, 5: -32.596062470203464, 6: 36.63885920652794, 7: -11.45736318836696, 8: -10.0841183490719}, {1: 20.43900574533479, 2: 5.559992311965079, 3: -9.405880259601133, 4: -13.812494193657038, 5: -2.9843588834679924, 6: -30.93792569144752, 7: 4.067124540341084, 8: 19.22638326732909}, -1.0943439080858024], 'ICU': [{1: -29.01549123213866, 2: 24.62908367097167, 3: -34.535204268240705, 4: -56.222620599982584, 5: 0.3188537168563581, 6: -22.224455079751387, 7: -10.238818926024031, 8: -1.918673959860314}, {1: 4.077575805492655, 2: 24.493214397776647, 3: 4.463700225578901, 4: 2.3385967457721435, 5: -4.247107039585577, 6: 16.496401288621836, 7: -21.124800409561416, 8: -7.472910821989823}, -14.866232193821347], 'SDU_WARD': [{1: -24.55805128192923, 2: -5.385866963941645, 3: -1.136434881954628, 4: 3.9080745018819947, 5: -3.3290713835921313, 6: -9.99116503833373, 7: -14.856653720124042, 8: -0.15758956858864437}, {1: -31.780430423615663, 2: -15.437165851233827, 3: 6.999450941561793, 4: 8.459871666640897, 5: 3.2907419475270725, 6: 7.722728870153489, 7: -4.204450148982254, 8: 11.480620352376903}, 69.68892929405638], 'GA': [{1: -28.379045482599125, 2: -11.54900248706895, 3: -13.767762154489791, 4: 8.238492976249841, 5: -22.77958600914853, 6: -31.31124854574118, 7: -10.802175165625862, 8: -12.341515419943024}, {1: -10.845237139713166, 2: -9.698631628525295, 3: -3.5427611783520003, 4: 7.405896387524539, 5: -4.150022410155678, 6: 33.18559728557773, 7: -35.61313529772893, 8: -2.128600221818145}, -19.202537209122333]}, 'WL': {'WL': [{1: -23.452449651953096, 2: -5.298830535794455, 3: 10.87366627511603, 4: -13.895065473335755, 5: -28.599499708951207, 6: -46.63603572443347, 7: 0.5629326418599945, 8: -12.569803629574974}, {1: -10.510947054842049, 2: 6.4235292338502195, 3: -4.094967951134104, 4: 28.755402449116247, 5: -10.974491711621855, 6: -35.50802859476657, 7: 1.9742482110734123, 8: -4.309938213799712}, -29.117074541781662]}}, 7: {'H_1': {'ED': [{1: -39.975806040033945, 2: -25.605573655762647, 3: -16.8027044867372, 4: 4.082036145274618, 5: -22.699000577455504, 6: 30.24971768403363, 7: -6.214184090363862, 8: -28.912200460909844}, {1: 11.242303594944923, 2: 23.865682988363734, 3: -32.26342443346202, 4: 19.678096865439365, 5: -5.911997319872263, 6: -14.24770926135729, 7: -21.571824981063024, 8: 15.180414148218436}, 36.04417368640097], 'OR': [{1: -0.2727712456510609, 2: -37.42087845745898, 3: 6.566296225668388, 4: -19.820762209417314, 5: -22.364881449190936, 6: -13.424138631289619, 7: -27.216877216543303, 8: -60.6060427308969}, {1: 7.911612613067394, 2: -27.168702385902257, 3: -29.898881736532545, 4: -29.51436075304709, 5: -31.838769739205887, 6: -56.16281676664796, 7: 2.251339560979881, 8: -56.42738341571514}, -58.937840440491726], 'ICU': [{1: -49.433574417421596, 2: -54.605944590094786, 3: -23.24344594332733, 4: -33.719630061223484, 5: -11.666673770109078, 6: -43.35916968873751, 7: -16.303917085491964, 8: -38.4639193811783}, {1: -67.86961871423766, 2: -14.817305884497713, 3: -27.736960374490238, 4: -17.69174507794701, 5: 6.198099709384909, 6: -44.60061886668838, 7: -54.70502424657827, 8: 4.733669028768741}, -28.33523294797327], 'SDU_WARD': [{1: 29.86555699423467, 2: -6.134348906410837, 3: 27.637286609163347, 4: -38.73634501354971, 5: -15.626944943947148, 6: -51.27493437878517, 7: 2.7935025705854883, 8: -4.380483069087461}, {1: -34.8047598331154, 2: -25.079299113117894, 3: -0.7757764331083195, 4: -21.470454306993133, 5: -12.025637885526262, 6: -9.805545103402608, 7: -28.06992002813246, 8: -7.3250828790199165}, 77.74790542379495], 'GA': [{1: -16.369168751324754, 2: -15.073157561663622, 3: -31.00943498191379, 4: -27.750744626389015, 5: -50.641231166243614, 6: -17.548400360135027, 7: 7.231144946630938, 8: -41.67939095045884}, {1: -37.07952172151103, 2: -36.47965964879462, 3: -25.03888880005515, 4: 1.3444046516493078, 5: -19.437656292787285, 6: -11.517966242706734, 7: -2.049541649884251, 8: -29.368677401533162}, 3.7709349793714804]}, 'WL': {'WL': [{1: 15.90746210952253, 2: -4.7771106582663805, 3: -28.593443707425116, 4: 6.228529345510543, 5: -25.341566766965965, 6: 5.340726684489617, 7: -23.51556184973095, 8: -1.9396517594163782}, {1: -18.331872711292124, 2: 15.872949900466052, 3: -56.770207687223746, 4: -28.541548479124977, 5: 2.5854547255899085, 6: -30.76679500043422, 7: -9.131396943858652, 8: -14.604184986413726}, -56.78398282075035]}}, 8: {'H_1': {'ED': [{1: -10.601429894258604, 2: 14.871038623648857, 3: -32.18620303459057, 4: -14.00030145501747, 5: 11.611068002711283, 6: -54.08544984696337, 7: -10.26478845760271, 8: 3.205605010500264}, {1: -31.988087771412342, 2: -42.209165799193066, 3: -26.172303184733313, 4: -12.996166841159408, 5: -18.74232194135005, 6: -13.925656487410423, 7: -31.237953078578553, 8: -20.729781547828846}, 36.33193202945627], 'OR': [{1: -51.8074002908095, 2: -64.67780622408803, 3: -27.05114559895573, 4: -18.083412605725886, 5: -7.09241184846015, 6: 14.258485327038017, 7: -20.29456512142552, 8: 3.741649242368865}, {1: -13.83410566644563, 2: -27.345568186911926, 3: -2.4084205156416054, 4: 9.97207533564422, 5: -19.976080765079452, 6: 14.853051677144569, 7: 5.416710016824403, 8: -16.25371554065906}, -31.40343266733994], 'ICU': [{1: 10.573387978657685, 2: 3.965768874922521, 3: -11.70726619618272, 4: -23.058432439063658, 5: 21.079345191791926, 6: 5.873719434100716, 7: -31.451862381003018, 8: -5.405980758658355}, {1: -29.747782926686384, 2: -30.838474210550245, 3: -14.957924294158984, 4: -2.392097752734175, 5: -26.88285792467655, 6: -34.852401469999556, 7: -25.70359603280852, 8: -20.617508282753843}, -6.763752763433059], 'SDU_WARD': [{1: 21.1294717898034, 2: 8.950112029738424, 3: 16.43183144274641, 4: 20.66278029593296, 5: -6.79115990706452, 6: -24.402455678779695, 7: -30.192757830314314, 8: 1.9131702782384234}, {1: -26.472867493807883, 2: -5.36991438964988, 3: 25.931131059450873, 4: -4.172543222092228, 5: -29.729938017326095, 6: -26.972549708414828, 7: -33.46259471509896, 8: 0.8597284854979996}, 100.648603476208], 'GA': [{1: -36.91924289968681, 2: 12.776806592990333, 3: 3.0647578739901675, 4: -2.3829471782139375, 5: -8.086730939856992, 6: -38.77236628572896, 7: 13.359062730456056, 8: -20.644050764133176}, {1: 34.53304882016443, 2: -35.80541188696543, 3: -13.700162211431245, 4: -16.727585995814493, 5: -14.985229085048381, 6: -4.626650919650116, 7: -50.88141622639768, 8: -21.156692844432634}, 4.465421694465913]}, 'WL': {'WL': [{1: -22.072291970918826, 2: -8.016922914305077, 3: -10.234443841950874, 4: -19.858170788185323, 5: -52.28045362648617, 6: -49.769725382908476, 7: -31.975852955744422, 8: -1.7782741846979224}, {1: 4.193047126641002, 2: -9.990966085910554, 3: -13.26665509995896, 4: 10.46024501735247, 5: -13.652740649408788, 6: -59.2615711796508, 7: -38.369195621070325, 8: -10.683013928553592}, -5.022648335607119]}}}


PARAMETROS_ESTRATEGIA_PROVISORIOS = {
    1: {
   "H_1" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
    "WL":{"WL":[{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]}
    },
   2: {
       "H_1" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 1, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 7, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 37, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 91],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
    },
    "WL":{"WL":[{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]}},
   3: {
       "H_1" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 1, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 7, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 37, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 91],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
    },
    "WL":{"WL":[{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]}},
   4: {
       "H_1" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 1, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 7, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 37, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 91],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
    },
    "WL":{"WL":[{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]}},
   5: {
       "H_1" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 1, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 7, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 37, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 91],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
    },
    "WL":{"WL":[{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]}},
   6: {
       "H_1" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 1, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 7, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 37, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 91],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
    },
    "WL":{"WL":[{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]}},
   7: {
       "H_1" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 1, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 7, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 37, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 91],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
    },
    "WL":{"WL":[{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]}},
   8: {
       "H_1" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 1, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 7, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 37, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 91],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
    },
    "WL":{"WL":[{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]}}
}
    