/** @file
 *****************************************************************************

 Implementation of interfaces for initializing MNT6.

 See mnt6_init.hpp .

 *****************************************************************************
 * @author     This file is part of libff, developed by SCIPR Lab
 *             and contributors (see AUTHORS).
 * @copyright  MIT license (see LICENSE file)
 *****************************************************************************/

#include <libff/algebra/curves/mnt/mnt6/mnt6_fields.hpp>

namespace libff {

void init_mnt6_fields()
{
    using bigint_r = bigint<mnt6_r_limbs>;
    using bigint_q = bigint<mnt6_q_limbs>;

    assert(sizeof(mp_limb_t) == 8 || sizeof(mp_limb_t) == 4); // Montgomery assumes this

    /* parameters for scalar field Fr */

    mnt6_modulus_r = bigint_r("475922286169261325753349249653048451545124879242694725395555128576210262817955800483758081");
    assert(mnt6_Fr::modulus_is_valid());
    if (sizeof(mp_limb_t) == 8)
    {
        mnt6_Fr::Rsquared = bigint_r("273000478523237720910981655601160860640083126627235719712980612296263966512828033847775776");
        mnt6_Fr::Rcubed = bigint_r("427298980065529822574935274648041073124704261331681436071990730954930769758106792920349077");
        mnt6_Fr::inv = 0xb071a1b67165ffff;
    }
    if (sizeof(mp_limb_t) == 4)
    {
        mnt6_Fr::Rsquared = bigint_r("273000478523237720910981655601160860640083126627235719712980612296263966512828033847775776");
        mnt6_Fr::Rcubed = bigint_r("427298980065529822574935274648041073124704261331681436071990730954930769758106792920349077");
        mnt6_Fr::inv = 0x7165ffff;
    }
    mnt6_Fr::num_bits = 298;
    mnt6_Fr::euler = bigint_r("237961143084630662876674624826524225772562439621347362697777564288105131408977900241879040");
    mnt6_Fr::s = 17;
    mnt6_Fr::t = bigint_r("3630998887399759870554727551674258816109656366292531779446068791017229177993437198515");
    mnt6_Fr::t_minus_1_over_2 = bigint_r("1815499443699879935277363775837129408054828183146265889723034395508614588996718599257");
    mnt6_Fr::multiplicative_generator = mnt6_Fr("17");
    mnt6_Fr::root_of_unity = mnt6_Fr("264706250571800080758069302369654305530125675521263976034054878017580902343339784464690243");
    mnt6_Fr::nqr = mnt6_Fr("17");
    mnt6_Fr::nqr_to_t = mnt6_Fr("264706250571800080758069302369654305530125675521263976034054878017580902343339784464690243");

    /* parameters for base field Fq */

    mnt6_modulus_q = bigint_q("475922286169261325753349249653048451545124878552823515553267735739164647307408490559963137");
    assert(mnt6_Fq::modulus_is_valid());
    if (sizeof(mp_limb_t) == 8)
    {
        mnt6_Fq::Rsquared = bigint_q("163983144722506446826715124368972380525894397127205577781234305496325861831001705438796139");
        mnt6_Fq::Rcubed = bigint_q("207236281459091063710247635236340312578688659363066707916716212805695955118593239854980171");
        mnt6_Fq::inv = 0xbb4334a3ffffffff;
    }
    if (sizeof(mp_limb_t) == 4)
    {
        mnt6_Fq::Rsquared = bigint_q("163983144722506446826715124368972380525894397127205577781234305496325861831001705438796139");
        mnt6_Fq::Rcubed = bigint_q("207236281459091063710247635236340312578688659363066707916716212805695955118593239854980171");
        mnt6_Fq::inv = 0xffffffff;
    }
    mnt6_Fq::num_bits = 298;
    mnt6_Fq::euler = bigint_q("237961143084630662876674624826524225772562439276411757776633867869582323653704245279981568");
    mnt6_Fq::s = 34;
    mnt6_Fq::t = bigint_q("27702323054502562488973446286577291993024111641153199339359284829066871159442729");
    mnt6_Fq::t_minus_1_over_2 = bigint_q("13851161527251281244486723143288645996512055820576599669679642414533435579721364");
    mnt6_Fq::multiplicative_generator = mnt6_Fq("10");
    mnt6_Fq::root_of_unity = mnt6_Fq("120638817826913173458768829485690099845377008030891618010109772937363554409782252579816313");
    mnt6_Fq::nqr = mnt6_Fq("5");
    mnt6_Fq::nqr_to_t = mnt6_Fq("406220604243090401056429458730298145937262552508985450684842547562990900634752279902740880");

    /* parameters for twist field Fq3 */

    mnt6_Fq3::euler = bigint<3*mnt6_q_limbs>("53898680178554951715397245154796036139463891589001478629193136369124915637741423690184935056189295242736833704290747216410090671804540908400210778934462129625646263095398323485795557551284190224166851571615834194321908328559167529729507439069424158411618728014749106176");
    mnt6_Fq3::s = 34;
    mnt6_Fq3::t = bigint<3*mnt6_q_limbs>("6274632199033507112809136178669989590936327770934612330653836993631547740397674926811006741620285348354004521888069251599964996777072188956687550402067383940523288107407084140669968625447269322370045302856694231080113482726640944570478452261237446033817102203");
    mnt6_Fq3::t_minus_1_over_2 = bigint<3*mnt6_q_limbs>("3137316099516753556404568089334994795468163885467306165326918496815773870198837463405503370810142674177002260944034625799982498388536094478343775201033691970261644053703542070334984312723634661185022651428347115540056741363320472285239226130618723016908551101");
    mnt6_Fq3::non_residue = mnt6_Fq("5");
    mnt6_Fq3::nqr = mnt6_Fq3(mnt6_Fq("5"),mnt6_Fq("0"),mnt6_Fq("0"));
    mnt6_Fq3::nqr_to_t = mnt6_Fq3(mnt6_Fq("154361449678783505076984156275977937654331103361174469632346230549735979552469642799720052"),mnt6_Fq("0"),mnt6_Fq("0"));
    mnt6_Fq3::Frobenius_coeffs_c1[0] = mnt6_Fq("1");
    mnt6_Fq3::Frobenius_coeffs_c1[1] = mnt6_Fq("471738898967521029133040851318449165997304108729558973770077319830005517129946578866686956");
    mnt6_Fq3::Frobenius_coeffs_c1[2] = mnt6_Fq("4183387201740296620308398334599285547820769823264541783190415909159130177461911693276180");
    mnt6_Fq3::Frobenius_coeffs_c2[0] = mnt6_Fq("1");
    mnt6_Fq3::Frobenius_coeffs_c2[1] = mnt6_Fq("4183387201740296620308398334599285547820769823264541783190415909159130177461911693276180");
    mnt6_Fq3::Frobenius_coeffs_c2[2] = mnt6_Fq("471738898967521029133040851318449165997304108729558973770077319830005517129946578866686956");

    /* parameters for Fq6 */

    mnt6_Fq6::euler = bigint<6*mnt6_q_limbs>("58101354499803048834583303220952913087824099988886273927160035716575561879937723707648335894925330628895188378773913275197213919452183382055206387082172181425605923957620009042449526418177025032365963902004248852434047609548572040108115533682304388051005201389178753450"
                                             "43409872160393969038819851306130935281801223313744881543615360884552109851303547212609185435570387523149780308979035592069180747953000755531869142327042207668768296881030935139706074910917829157651610581536611575608256606920332948110215549184448842466566234011340898304");
    mnt6_Fq6::s = 35;
    mnt6_Fq6::t = bigint<6*mnt6_q_limbs>("33819439413376995848132823140449422113495005753872842718358172404449178068862368648201422704689513559508596301762103845363723765739812155984811477294524771525528004833974415111849972988814712171655825747877969902727082144439087738345910057939067708823716501582634375343"
                                         "5847458438970728837816268863746135919459701010127603166248612157334114299813724775601247409100783262585160573302944865547422130356601017732864079433903226609619351620845900332770896779310297521160194334896316959965523367684819557943277500405933756990507607931");
    mnt6_Fq6::t_minus_1_over_2 = bigint<6*mnt6_q_limbs>("16909719706688497924066411570224711056747502876936421359179086202224589034431184324100711352344756779754298150881051922681861882869906077992405738647262385762764002416987207555924986494407356085827912873938984951363541072219543869172955028969533854411858250791317187671"
                                                        "7923729219485364418908134431873067959729850505063801583124306078667057149906862387800623704550391631292580286651472432773711065178300508866432039716951613304809675810422950166385448389655148760580097167448158479982761683842409778971638750202966878495253803965");
    mnt6_Fq6::non_residue = mnt6_Fq("5");
    mnt6_Fq6::nqr = mnt6_Fq6(mnt6_Fq3(mnt6_Fq("2"),mnt6_Fq("0"),mnt6_Fq("0")),mnt6_Fq3::one());
    mnt6_Fq6::nqr_to_t = mnt6_Fq6(mnt6_Fq3::zero(),mnt6_Fq3(mnt6_Fq("0"),mnt6_Fq("95371092960829291863271933246328602470562937077363363183769791678780911004969735451493071"),mnt6_Fq("0")));
    mnt6_Fq6::Frobenius_coeffs_c1[0] = mnt6_Fq("1");
    mnt6_Fq6::Frobenius_coeffs_c1[1] = mnt6_Fq("471738898967521029133040851318449165997304108729558973770077319830005517129946578866686957");
    mnt6_Fq6::Frobenius_coeffs_c1[2] = mnt6_Fq("471738898967521029133040851318449165997304108729558973770077319830005517129946578866686956");
    mnt6_Fq6::Frobenius_coeffs_c1[3] = mnt6_Fq("475922286169261325753349249653048451545124878552823515553267735739164647307408490559963136");
    mnt6_Fq6::Frobenius_coeffs_c1[4] = mnt6_Fq("4183387201740296620308398334599285547820769823264541783190415909159130177461911693276180");
    mnt6_Fq6::Frobenius_coeffs_c1[5] = mnt6_Fq("4183387201740296620308398334599285547820769823264541783190415909159130177461911693276181");
    mnt6_Fq6::my_Fp2::non_residue = mnt6_Fq3::non_residue;
}

} // namespace libff