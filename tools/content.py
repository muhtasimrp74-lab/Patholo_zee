# -*- coding: utf-8 -*-
"""New topics for the whole-pathology expansion: General Pathology (GP) and Haematology (HM).
Written in the same HTML shape as the existing answers so the site's JS (Say-this-first box, search,
related questions, practice mode) treats them exactly like the original 189."""
import re, html

def esc(t):
    t = html.escape(t, quote=False)
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)

def P(label, text=None):
    if text is None:
        return '<p>%s</p>' % esc(label)
    return '<p><strong class="lbl">%s:</strong> %s</p>' % (esc(label), esc(text))

def SH(t):
    return '<div class="sh"><strong class="lbl">%s</strong></div>' % esc(t)

def UL(items):
    return '<ul>' + ''.join('<li>%s</li>' % esc(i) for i in items) + '</ul>'

def TB(head, rows):
    h = ''.join('<th>%s</th>' % esc(x) for x in head)
    b = ''
    for r in rows:
        b += '<tr><td><strong>%s</strong></td>' % esc(r[0]) + ''.join('<td>%s</td>' % esc(x) for x in r[1:]) + '</tr>'
    return '<div class="tw"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (h, b)

# (topic id, topic name, part, [ (code, question, answer-html) ... ])
TOPICS = []

# ------------------------------------------------------------------ 16 Cell injury
TOPICS.append(('16', 'Cell Injury, Adaptation and Death', 'GP', [
('GP', 'Define hypertrophy, hyperplasia, atrophy and metaplasia. Give examples.',
 P('Cellular adaptations', 'Reversible functional and structural responses of cells to stress or stimuli. If the limit of adaptation is exceeded, cell injury follows.') +
 TB(['Adaptation', 'Definition', 'Examples'], [
  ['Hypertrophy', 'Increase in the **size** of cells, and so of the organ. No new cells are formed.', 'Cardiac muscle in hypertension or aortic stenosis; gravid uterus (also hyperplasia); skeletal muscle of athletes'],
  ['Hyperplasia', 'Increase in the **number** of cells in an organ or tissue. Occurs in cells able to divide.', 'Physiological: breast at puberty and pregnancy, liver regeneration. Pathological: endometrial hyperplasia (excess oestrogen), benign prostatic hyperplasia'],
  ['Atrophy', 'Decrease in cell size and number through reduced protein synthesis and increased degradation (ubiquitin-proteasome pathway, autophagy).', 'Disuse, denervation, ischaemia, malnutrition, loss of hormonal stimulation, pressure, ageing (brain, heart)'],
  ['Metaplasia', 'Reversible **replacement of one mature cell type by another** mature cell type, through reprogramming of stem cells.', 'Columnar to squamous in the bronchus of smokers; squamous to columnar in Barrett oesophagus; vitamin A deficiency; myositis ossificans'],
 ]) +
 SH('If pushed') + P('Metaplasia carries a risk of progressing to dysplasia and then carcinoma if the stimulus persists. Hypertrophy and hyperplasia often occur together.')),

('GP', 'Differentiate reversible from irreversible cell injury. Describe the morphology.',
 P('Reversible injury', 'Injury in which cell function and morphology can return to normal if the stimulus is removed. **Irreversible injury** progresses to cell death (necrosis or apoptosis).') +
 SH('Causes of cell injury') +
 UL(['Hypoxia and ischaemia (the commonest)', 'Physical agents: trauma, heat, cold, radiation, electric shock', 'Chemicals and drugs; toxins', 'Infectious agents', 'Immunological reactions', 'Genetic derangements and nutritional imbalances']) +
 TB(['Feature', 'Reversible', 'Irreversible'], [
  ['Light microscopy', 'Cell swelling (hydropic change), fatty change', 'Increased eosinophilia, nuclear changes: pyknosis, karyorrhexis, karyolysis'],
  ['Electron microscopy', 'Plasma membrane blebs, ER dilation, ribosome detachment, mitochondrial swelling, chromatin clumping', 'Mitochondrial amorphous densities, rupture of membranes and lysosomes, myelin figures'],
  ['Key mechanism', 'ATP depletion, failure of the Na+/K+ pump with influx of water', 'Irreversible mitochondrial damage and profound loss of membrane function'],
  ['Outcome', 'Recovery', 'Necrosis, release of enzymes (e.g. troponin, CK-MB in myocardial infarction)'],
 ]) +
 SH('If pushed') + P('The two hallmarks that mark the point of no return are the inability to reverse mitochondrial dysfunction (loss of oxidative phosphorylation) and profound disturbances of membrane function.')),

('GP', 'Differentiate necrosis from apoptosis. Describe the types of necrosis.',
 P('Necrosis', 'Death of cells in a living organism through uncontrolled injury, with loss of membrane integrity, leakage of contents and an inflammatory reaction. **Apoptosis** is programmed, energy-dependent cell death without inflammation.') +
 TB(['Feature', 'Necrosis', 'Apoptosis'], [
  ['Cell size', 'Enlarged (swelling)', 'Reduced (shrinkage)'],
  ['Nucleus', 'Pyknosis, karyorrhexis, karyolysis', 'Fragmentation into nucleosome-sized pieces (DNA ladder)'],
  ['Plasma membrane', 'Disrupted', 'Intact, altered (phosphatidylserine flipped outwards)'],
  ['Cell contents', 'Enzymatic digestion and leakage', 'Apoptotic bodies, phagocytosed by neighbours'],
  ['Inflammation', 'Frequent', 'Absent'],
  ['Extent', 'Groups of cells', 'Single cells'],
  ['Role', 'Always pathological', 'Physiological (embryogenesis, involution) or pathological'],
 ]) +
 SH('Types of necrosis') +
 TB(['Type', 'Typical setting and feature'], [
  ['Coagulative', 'Ischaemia in solid organs (heart, kidney, spleen). Architecture preserved for some days. Brain is the exception.'],
  ['Liquefactive', 'Bacterial and fungal infections (abscess) and brain infarcts. Tissue turns to liquid.'],
  ['Caseous', 'Tuberculosis. Cheese-like, amorphous, granular debris surrounded by a granulomatous border.'],
  ['Fat necrosis', 'Enzymatic (acute pancreatitis, with saponification) or traumatic (breast).'],
  ['Fibrinoid', 'Immune-mediated vasculitis and malignant hypertension. Bright pink fibrin-like deposit in vessel walls.'],
  ['Gangrenous', 'Limb ischaemia. Dry (coagulative), wet (with infection, liquefactive) and gas gangrene (Clostridium).'],
 ])),

('GP', 'What is dystrophic calcification? How does it differ from metastatic calcification?',
 P('Calcification', 'Abnormal deposition of calcium salts in tissues. **Dystrophic** calcification occurs in dead or dying tissue with normal serum calcium. **Metastatic** calcification occurs in normal tissue because of hypercalcaemia.') +
 TB(['Feature', 'Dystrophic', 'Metastatic'], [
  ['Tissue', 'Necrotic or damaged', 'Normal'],
  ['Serum calcium', 'Normal', 'Raised'],
  ['Examples', 'Atheromatous plaques, damaged heart valves (calcific aortic stenosis), tuberculous lymph nodes, fat necrosis, some tumours (psammoma bodies)', 'Kidney, lungs, gastric mucosa, systemic arteries and pulmonary veins'],
  ['Causes', 'Local tissue injury', 'Hyperparathyroidism, vitamin D intoxication, bone destruction (metastases, myeloma), chronic renal failure'],
  ['Clinical effect', 'Often stiffens tissue (valves, vessels)', 'Usually silent, may cause organ dysfunction'],
 ]) +
 SH('Demonstration') + P('Haematoxylin and eosin shows basophilic granular deposits. Special stains: von Kossa (black) and alizarin red (red-orange).')),
]))

# ------------------------------------------------------------------ 17 Inflammation and repair
TOPICS.append(('17', 'Inflammation and Repair', 'GP', [
('GP', 'What are the cardinal signs of acute inflammation? Describe the vascular events.',
 P('Acute inflammation', 'A rapid, short-lived response of vascularised tissue to infection or injury, with exudation of fluid and plasma proteins and emigration of leukocytes, chiefly neutrophils.') +
 SH('Cardinal signs') + UL(['Rubor (redness)', 'Calor (heat)', 'Tumor (swelling)', 'Dolor (pain): these four are from Celsus', 'Functio laesa (loss of function): added by Virchow']) +
 SH('Vascular events') +
 UL(['Transient vasoconstriction, followed by **vasodilation** (histamine, nitric oxide) causing increased blood flow (redness and warmth).',
     '**Increased vascular permeability** with escape of protein-rich fluid (exudate) into tissue, causing swelling.',
     'Stasis of blood as the fluid leaves, with concentration of red cells and leukocyte margination.']) +
 TB(['Mechanism of increased permeability', 'Features'], [
  ['Endothelial contraction', 'Histamine, bradykinin, leukotrienes. Immediate and short-lived, in venules.'],
  ['Direct endothelial injury', 'Burns, toxins. Immediate and sustained.'],
  ['Leukocyte-mediated injury', 'Leukocyte enzymes and ROS. Late, in venules and capillaries.'],
  ['Increased transcytosis', 'VEGF raises the number of channels.'],
 ]) +
 SH('Exudate versus transudate') + P('Exudate: protein above 3 g/dL, specific gravity above 1.020, cells present (inflammation). Transudate: low protein, specific gravity below 1.012, no inflammation (e.g. heart failure).')),

('GP', 'Describe the steps of leukocyte recruitment in acute inflammation.',
 P('Leukocyte recruitment', 'Leukocytes (mainly neutrophils early, monocytes later) leave the blood and reach the site of injury through a sequence of steps in post-capillary venules.') +
 TB(['Step', 'Mechanism', 'Molecules'], [
  ['1. Margination and rolling', 'Cells move to the vessel periphery and roll with weak, transient adhesion', 'Selectins: E-selectin and P-selectin (endothelium), L-selectin (leukocyte); sialyl Lewis X'],
  ['2. Firm adhesion', 'Cytokines (TNF, IL-1) raise integrin affinity and endothelial ligand expression', 'Integrins LFA-1 and Mac-1 with ICAM-1; VLA-4 with VCAM-1'],
  ['3. Transmigration (diapedesis)', 'Leukocytes squeeze between endothelial cells, mainly in venules', 'PECAM-1 (CD31)'],
  ['4. Chemotaxis', 'Movement along a chemical gradient to the site', 'Bacterial products (formylated peptides), IL-8, C5a, leukotriene B4'],
 ]) +
 SH('After arrival') + P('Recognition, phagocytosis, and killing by oxygen-dependent (ROS, myeloperoxidase) and oxygen-independent mechanisms.') +
 SH('If pushed') + P('Leukocyte adhesion deficiency type 1 is caused by a defect of the CD18 integrin subunit, giving recurrent bacterial infections, delayed umbilical cord separation and marked neutrophilia.')),

('GP', 'Define chronic inflammation. What is a granuloma? Give causes and morphology.',
 P('Chronic inflammation', 'Inflammation of prolonged duration (weeks to months) in which inflammation, tissue destruction and attempts at repair proceed together. It is characterised by mononuclear cells: macrophages, lymphocytes and plasma cells, with fibrosis and new vessels.') +
 SH('Granuloma') +
 P('Granuloma', 'A focus of chronic inflammation made of aggregated activated macrophages (epithelioid cells), often with multinucleate giant cells, surrounded by a collar of lymphocytes.') +
 UL(['Mechanism: Th1 cells secrete IFN-gamma, which transforms macrophages into epithelioid cells.',
     'Giant cells: Langhans type (nuclei in a horseshoe at the periphery, in immune granulomas such as TB) and foreign-body type (nuclei scattered).',
     'Centre may show caseous necrosis (tuberculosis) or be non-necrotising (sarcoidosis).']) +
 TB(['Group', 'Causes'], [
  ['Infections', 'Tuberculosis (caseating), leprosy, syphilis (gumma), fungal infections, schistosomiasis, cat-scratch disease'],
  ['Immune', 'Sarcoidosis, Crohn disease'],
  ['Foreign body', 'Suture material, talc, silica, beryllium'],
 ])),

('GP', 'Describe wound healing. Differentiate healing by primary and secondary intention. What factors influence healing?',
 P('Wound healing', 'Restoration of tissue architecture and function after injury, by regeneration or by repair with scar formation.') +
 SH('Phases') +
 UL(['**Haemostasis and inflammation:** clot formation, neutrophils at about 24 hours, macrophages by day 3.',
     '**Proliferation:** granulation tissue (new capillaries and fibroblasts) from day 3 to 5, re-epithelialisation.',
     '**Remodelling:** collagen deposition and cross-linking, wound contraction by myofibroblasts. Tensile strength reaches about 10% at one week and about 70 to 80% by three months.']) +
 TB(['Feature', 'Primary intention', 'Secondary intention'], [
  ['Wound', 'Clean, surgical incision; edges approximated by sutures', 'Large defect; edges apart; tissue loss'],
  ['Clot and necrosis', 'Minimal', 'More, with intense inflammation'],
  ['Granulation tissue', 'Scanty', 'Abundant'],
  ['Contraction', 'Little', 'Marked (myofibroblasts)'],
  ['Scar', 'Thin', 'Large, may cause contracture'],
  ['Healing time', 'Short', 'Prolonged'],
 ]) +
 SH('Factors affecting healing') +
 UL(['Local: infection, foreign body, poor blood supply, mechanical stress, size and site of the wound.',
     'Systemic: age, diabetes mellitus, malnutrition (protein, vitamin C, zinc), corticosteroids, anaemia.']) +
 SH('Complications') + P('Wound dehiscence, infection, keloid and hypertrophic scar, contracture, excessive granulation tissue, incisional hernia.')),
]))

# ------------------------------------------------------------------ 18 Haemodynamics
TOPICS.append(('18', 'Haemodynamic Disorders, Thrombosis and Shock', 'GP', [
('GP', 'What is thrombosis? Explain Virchow triad and the fate of a thrombus.',
 P('Thrombosis', 'Formation of a solid mass from blood constituents within the vessels or heart of a living person.') +
 SH('Virchow triad') +
 TB(['Component', 'Examples'], [
  ['Endothelial injury', 'Atherosclerosis, myocardial infarction, vasculitis, hypertension, smoking, trauma, toxins'],
  ['Abnormal blood flow', 'Stasis (atrial fibrillation, immobilisation, varicose veins, aneurysm) or turbulence'],
  ['Hypercoagulability', 'Primary: factor V Leiden, prothrombin gene mutation, deficiency of antithrombin III, protein C or protein S. Secondary: cancer, pregnancy, oral contraceptives, nephrotic syndrome, antiphospholipid syndrome, heparin-induced thrombocytopenia'],
 ]) +
 SH('Morphology') + P('Lines of Zahn (alternating pale platelet and fibrin layers and dark red cell layers) distinguish a thrombus formed in life from a postmortem clot. Arterial thrombi are usually occlusive and pale; venous thrombi form in stasis and are red (red cells trapped in fibrin).') +
 SH('Fate of a thrombus') +
 UL(['Propagation', 'Embolisation', 'Dissolution (fibrinolysis, in fresh thrombi)', 'Organisation and recanalisation', 'Infection, giving a septic thrombus or mycotic aneurysm'])),

('GP', 'Define embolism. Types of embolism. Describe pulmonary thromboembolism.',
 P('Embolism', 'Detachment and transport of an intravascular solid, liquid or gaseous mass (embolus) carried by blood to a site distant from its origin.') +
 TB(['Type', 'Source and note'], [
  ['Thromboembolism', 'About 99% of emboli. Most pulmonary emboli come from deep leg veins; systemic emboli come from the left heart.'],
  ['Fat embolism', 'Fracture of long bones or soft-tissue trauma. Triad of pulmonary insufficiency, neurological symptoms and thrombocytopenia with petechial rash, 1 to 3 days after injury.'],
  ['Air embolism', 'More than about 100 mL entering the circulation (surgery, trauma, childbirth). Decompression sickness is gas (nitrogen) emboli.'],
  ['Amniotic fluid embolism', 'Obstetric complication with sudden respiratory failure and DIC.'],
  ['Others', 'Tumour, bone marrow, foreign material, atheroembolism (cholesterol)'],
 ]) +
 SH('Pulmonary thromboembolism') +
 UL(['Source: deep vein thrombosis of the leg (popliteal, femoral, iliac veins).',
     'Large embolus lodged at the bifurcation of the pulmonary trunk (saddle embolus) can cause sudden death or acute right heart failure.',
     'Medium emboli often cause no infarct because of the dual (bronchial) blood supply; infarction occurs in a minority, especially with left heart failure.',
     'Multiple small emboli over time lead to pulmonary hypertension.'])),

('GP', 'Define infarction. Differentiate red from white infarcts.',
 P('Infarction', 'An area of ischaemic coagulative necrosis caused by occlusion of the arterial supply or venous drainage of a tissue. The commonest cause is arterial thrombosis or embolism.') +
 TB(['Feature', 'White (pale) infarct', 'Red (haemorrhagic) infarct'], [
  ['Cause', 'Arterial occlusion', 'Venous occlusion, or arterial occlusion in loose tissue or tissue with dual circulation'],
  ['Organs', 'Solid organs with end-arteries: heart, spleen, kidney', 'Lung, intestine, ovary, testis (torsion), brain (venous), previously congested tissue'],
  ['Appearance', 'Pale, wedge-shaped, apex towards the occluded vessel', 'Dark red, wedge-shaped, haemorrhagic'],
 ]) +
 SH('Factors that influence the outcome') + UL(['Nature of the vascular supply', 'Rate of development of the occlusion', 'Vulnerability of the tissue to hypoxia (neurons most, fibroblasts least)', 'Oxygen content of blood']) +
 SH('If pushed') + P('Brain infarcts undergo liquefactive necrosis, other solid organs coagulative necrosis. A septic infarct results from infected emboli and may form an abscess.')),

('GP', 'Define shock. Classify it. Describe the stages of shock.',
 P('Shock', 'A state of systemic hypoperfusion due to reduced cardiac output or reduced effective circulating blood volume, leading to hypotension and impaired tissue perfusion with cellular hypoxia.') +
 TB(['Type', 'Cause'], [
  ['Cardiogenic', 'Failure of the pump: myocardial infarction, arrhythmia, tamponade, pulmonary embolism'],
  ['Hypovolaemic', 'Loss of blood or fluid: haemorrhage, burns, vomiting, diarrhoea (cholera)'],
  ['Septic', 'Overwhelming microbial infection: bacterial endotoxin, TNF, IL-1, nitric oxide, DIC'],
  ['Others', 'Anaphylactic (IgE-mediated vasodilation) and neurogenic (loss of vascular tone)'],
 ]) +
 SH('Stages') +
 UL(['**Non-progressive (compensated):** reflex compensatory mechanisms (tachycardia, vasoconstriction) maintain vital organ perfusion.',
     '**Progressive:** tissue hypoperfusion with lactic acidosis, worsening circulatory failure.',
     '**Irreversible:** cellular and tissue injury so severe that survival is not possible even if the haemodynamics are corrected.']) +
 SH('Morphology (shock organs)') + P('Brain: ischaemic encephalopathy. Heart: coagulative or contraction band necrosis. Lung: diffuse alveolar damage. Kidney: acute tubular necrosis. Gut: haemorrhagic enteropathy. Liver: centrilobular necrosis. Adrenal: cortical lipid depletion.')),

('GP', 'What is oedema? Describe its pathogenesis.',
 P('Oedema', 'Accumulation of excess fluid in the interstitial tissue spaces (anasarca when generalised and severe; effusion when in body cavities).') +
 TB(['Mechanism', 'Examples'], [
  ['Increased hydrostatic pressure', 'Congestive cardiac failure, venous obstruction (deep vein thrombosis), cirrhosis with portal hypertension'],
  ['Reduced plasma oncotic pressure (hypoalbuminaemia)', 'Nephrotic syndrome, cirrhosis, protein-losing enteropathy, malnutrition'],
  ['Lymphatic obstruction', 'Filariasis, malignant infiltration, post-surgery or radiation'],
  ['Sodium and water retention', 'Renal failure, excess salt intake, activation of the renin-angiotensin system'],
  ['Increased vascular permeability', 'Inflammation (exudate), burns'],
 ]) +
 SH('Transudate versus exudate') + P('Transudate is protein-poor (below 3 g/dL) and non-inflammatory; exudate is protein-rich and inflammatory.')),
]))

# ------------------------------------------------------------------ 19 Neoplasia
TOPICS.append(('19', 'Neoplasia', 'GP', [
('GP', 'Define neoplasia. Differentiate benign from malignant tumours.',
 P('Neoplasia', 'Abnormal, excessive, uncoordinated and purposeless growth of cells that persists after the stimulus has stopped. A neoplasm is a mass of such tissue.') +
 TB(['Feature', 'Benign', 'Malignant'], [
  ['Differentiation', 'Well differentiated; resembles tissue of origin', 'Variable; may be anaplastic (loss of differentiation)'],
  ['Growth rate', 'Slow', 'Usually rapid'],
  ['Local invasion', 'Cohesive, expansile, often encapsulated', 'Infiltrative; no true capsule'],
  ['Metastasis', 'Absent', 'Frequent (the most reliable feature)'],
  ['Nuclei', 'Normal or minimal atypia; few mitoses', 'Pleomorphism, hyperchromasia, high nuclear-cytoplasmic ratio, atypical mitoses'],
  ['Recurrence after excision', 'Uncommon', 'Common'],
  ['Effect on host', 'Usually mild (pressure, hormones)', 'Cachexia, destruction, death'],
 ]) +
 SH('Terms') + UL(['**Dysplasia:** disordered growth with loss of uniformity and architecture; may be pre-malignant.', '**Carcinoma in situ:** full-thickness dysplasia without invasion of the basement membrane.', '**Anaplasia:** lack of differentiation, the hallmark of malignancy.'])),

('GP', 'What are oncogenes and tumour suppressor genes? Give examples.',
 P('Oncogene', 'A mutated or overexpressed form of a normal growth-promoting gene (proto-oncogene) that gives cells autonomous growth. Tumour suppressor genes normally restrain growth, and **both alleles** must be lost for cancer to develop (Knudson two-hit hypothesis).') +
 TB(['Group', 'Gene', 'Mechanism and tumour'], [
  ['Oncogenes', 'RAS', 'Point mutation; the commonest oncogene abnormality in human cancer'],
  ['', 'MYC', 'Translocation t(8;14) in Burkitt lymphoma'],
  ['', 'BCR-ABL', 'Translocation t(9;22) in chronic myeloid leukaemia'],
  ['', 'HER2 (ERBB2)', 'Amplification in breast cancer'],
  ['', 'BCL2', 'Translocation t(14;18) in follicular lymphoma; blocks apoptosis'],
  ['Tumour suppressors', 'RB', 'Gatekeeper of the cell cycle (G1/S); retinoblastoma, osteosarcoma'],
  ['', 'TP53', 'Guardian of the genome; most common mutated gene in cancer; Li-Fraumeni syndrome'],
  ['', 'APC', 'Familial adenomatous polyposis and colorectal cancer'],
  ['', 'BRCA1 and BRCA2', 'Hereditary breast and ovarian cancer'],
  ['', 'NF1, VHL, WT1', 'Neurofibromatosis type 1, von Hippel-Lindau disease, Wilms tumour'],
 ]) +
 SH('Hallmarks of cancer') + P('Self-sufficiency in growth signals, insensitivity to growth-inhibitory signals, evasion of apoptosis, limitless replicative potential (telomerase), sustained angiogenesis, invasion and metastasis, altered metabolism, and evasion of immune destruction. Genomic instability and inflammation are enabling characteristics.')),

('GP', 'Describe the routes and the mechanism of metastasis.',
 P('Metastasis', 'Spread of a tumour to sites physically discontinuous with the primary tumour. It marks a tumour as malignant.') +
 TB(['Route', 'Notes'], [
  ['Lymphatic', 'Typical of carcinomas. First the regional (sentinel) node. Example: breast carcinoma to axillary nodes.'],
  ['Haematogenous', 'Typical of sarcomas, also renal cell carcinoma and hepatocellular carcinoma (venous invasion). Commonest sites: liver and lungs; bone via the vertebral venous plexus (prostate).'],
  ['Transcoelomic (seeding)', 'Spread across peritoneal, pleural or pericardial cavities. Ovarian carcinoma.'],
  ['Implantation', 'Rare; along a needle track or surgical scar.'],
 ]) +
 SH('Steps of the invasion-metastasis cascade') +
 UL(['Loosening of cell-cell contacts (loss of E-cadherin).', 'Degradation of the basement membrane and matrix (matrix metalloproteinases).', 'Changes in attachment to matrix (integrins) and migration.', 'Intravasation, survival in the circulation, arrest and extravasation.', 'Colonisation of the new site (seed and soil).'])),

('GP', 'Explain grading and staging of cancer.',
 P('Grading and staging', 'Two methods of estimating the clinical aggressiveness and the extent of a cancer, used together for prognosis and treatment.') +
 TB(['', 'Grading', 'Staging'], [
  ['Based on', 'Degree of differentiation and number of mitoses (microscopy)', 'Size of primary and extent of spread in the body'],
  ['Categories', 'Grade I (well), II (moderate), III (poor), IV (undifferentiated)', 'TNM system: T (tumour size or extent), N (lymph node involvement), M (distant metastasis)'],
  ['Value', 'Predicts behaviour, correlates only loosely with outcome', 'The more important prognostic factor'],
 ]) +
 SH('If pushed') + P('Stage groups (I to IV) are derived from the TNM categories. The absence of distant metastasis (M0) and nodal disease (N0) is favourable.')),
]))

# ------------------------------------------------------------------ 20 Immunopathology & genetics
TOPICS.append(('20', 'Immunopathology and Genetic Disorders', 'GP', [
('GP', 'Classify hypersensitivity reactions with examples.',
 P('Hypersensitivity', 'Excessive or inappropriate immune responses that cause tissue injury. Classified (Gell and Coombs) into four types.') +
 TB(['Type', 'Mechanism', 'Examples'], [
  ['I: Immediate (anaphylactic)', 'IgE bound to mast cells; antigen exposure releases histamine and mediators within minutes', 'Anaphylaxis, allergic rhinitis, asthma, urticaria, food allergy'],
  ['II: Antibody-mediated', 'IgG or IgM against cell-surface or matrix antigens; complement, opsonisation, or altered cell function', 'Transfusion reaction, haemolytic disease of the newborn, autoimmune haemolytic anaemia, Goodpasture syndrome, myasthenia gravis, Graves disease'],
  ['III: Immune complex', 'Antigen-antibody complexes deposit in tissues and activate complement', 'Serum sickness, SLE, post-streptococcal glomerulonephritis, Arthus reaction, polyarteritis nodosa'],
  ['IV: Cell-mediated (delayed)', 'Sensitised T cells: CD4+ cytokine release, or CD8+ cytotoxicity; 24 to 72 hours', 'Tuberculin (Mantoux) test, contact dermatitis, granulomatous inflammation, graft rejection'],
 ])),

('GP', 'What is amyloidosis? Classify it. How is it demonstrated?',
 P('Amyloidosis', 'A group of disorders in which misfolded proteins are deposited extracellularly as insoluble fibrils with a cross-beta-pleated sheet structure, damaging tissue.') +
 TB(['Type', 'Protein', 'Setting'], [
  ['AL (primary)', 'Immunoglobulin light chains', 'Plasma cell dyscrasias, multiple myeloma'],
  ['AA (secondary)', 'Serum amyloid A', 'Chronic inflammation: tuberculosis, rheumatoid arthritis, bronchiectasis, chronic osteomyelitis'],
  ['Dialysis-related', 'Beta-2 microglobulin', 'Long-term haemodialysis'],
  ['Hereditary and senile', 'Transthyretin', 'Familial amyloid polyneuropathy; senile cardiac amyloid'],
  ['Localised', 'Abeta (Alzheimer disease), calcitonin (medullary thyroid carcinoma), islet amyloid polypeptide (type 2 diabetes)', 'Organ-specific'],
 ]) +
 SH('Demonstration') +
 UL(['H&E: amorphous, eosinophilic, hyaline extracellular material.', '**Congo red:** pink-red, with **apple-green birefringence** under polarised light (diagnostic).', 'Electron microscopy: non-branching fibrils, 7.5 to 10 nm.', 'Biopsy sites: kidney, rectum, gingiva, abdominal fat pad.']) +
 SH('Organs involved') + P('Kidney (the commonest, nephrotic syndrome), heart (restrictive cardiomyopathy), spleen (sago or lardaceous), liver, tongue, nerves.')),

('GP', 'Describe Down syndrome: cytogenetics and clinical features.',
 P('Down syndrome', 'The commonest chromosomal disorder, caused by trisomy 21 (extra copy of chromosome 21).') +
 TB(['Mechanism', 'Frequency', 'Note'], [
  ['Meiotic non-disjunction (trisomy 21; 47,XX,+21 or 47,XY,+21)', 'About 95%', 'Risk rises with maternal age'],
  ['Robertsonian translocation (often 14;21)', 'About 4%', 'May be familial; recurrence risk is higher'],
  ['Mosaicism', 'About 1%', 'Milder features'],
 ]) +
 SH('Clinical features') +
 UL(['Intellectual disability, hypotonia', 'Flat facies, epicanthic folds, upslanting palpebral fissures, Brushfield spots, protruding tongue', 'Single palmar (simian) crease', 'Congenital heart disease (endocardial cushion defects: atrioventricular septal defect)', 'Duodenal atresia', 'Increased risk of acute leukaemia and early Alzheimer disease', 'Hypothyroidism and atlantoaxial instability']) +
 SH('Prenatal screening') + P('Raised nuchal translucency, and in the maternal serum a low AFP, low unconjugated oestriol, high hCG and high inhibin A. Confirm by karyotyping.')),

('GP', 'Describe the patterns of Mendelian inheritance with examples.',
 P('Mendelian disorders', 'Disorders caused by a single gene defect, with predictable inheritance patterns.') +
 TB(['Pattern', 'Features', 'Examples'], [
  ['Autosomal dominant', 'Vertical transmission; both sexes affected; usually structural or receptor protein defects', 'Marfan syndrome, familial hypercholesterolaemia, Huntington disease, neurofibromatosis, adult polycystic kidney disease, achondroplasia'],
  ['Autosomal recessive', 'Horizontal transmission (siblings); consanguinity; usually enzyme defects; both parents carriers', 'Cystic fibrosis, sickle cell disease, thalassaemia, phenylketonuria, Gaucher disease'],
  ['X-linked recessive', 'Males affected; carrier mothers; no male-to-male transmission', 'Haemophilia A and B, Duchenne muscular dystrophy, G6PD deficiency'],
  ['X-linked dominant', 'Affected fathers pass to all daughters, none of the sons', 'Vitamin D-resistant rickets'],
 ]) +
 SH('If pushed') + P('Genes with variable expressivity or reduced penetrance can make autosomal dominant disorders appear to skip a generation.')),
]))

# ------------------------------------------------------------------ 21 Red cell disorders
TOPICS.append(('21', 'Red Cell Disorders and Anaemias', 'HM', [
('HM', 'Define anaemia. Classify anaemias morphologically with examples.',
 P('Anaemia', 'Reduction in haemoglobin concentration (or red cell mass) below the normal range for age and sex: below about 13 g/dL in adult men and 12 g/dL in non-pregnant women.') +
 TB(['Morphology', 'MCV', 'Examples'], [
  ['Microcytic hypochromic', 'Below 80 fL', 'Iron deficiency anaemia, thalassaemia, sideroblastic anaemia, anaemia of chronic disease (some)'],
  ['Normocytic normochromic', '80 to 100 fL', 'Acute blood loss, haemolytic anaemias, aplastic anaemia, anaemia of chronic disease, chronic kidney disease'],
  ['Macrocytic', 'Above 100 fL', 'Megaloblastic (vitamin B12 and folate deficiency); non-megaloblastic (alcoholism, liver disease, hypothyroidism, reticulocytosis)'],
 ]) +
 SH('Etiological classification') + UL(['Blood loss (acute or chronic)', 'Increased destruction (haemolysis)', 'Impaired production: nutritional deficiency, marrow failure, chronic disease']) +
 SH('Investigations') + P('Complete blood count with indices, reticulocyte count, peripheral smear, then iron studies, vitamin B12 and folate, haemoglobin electrophoresis or bone marrow examination as indicated.')),

('HM', 'Iron deficiency anaemia: causes, laboratory findings and morphology.',
 P('Iron deficiency anaemia', 'A microcytic hypochromic anaemia caused by inadequate iron for haemoglobin synthesis. It is the commonest anaemia worldwide.') +
 SH('Causes') +
 UL(['Chronic blood loss: gastrointestinal (peptic ulcer, hookworm infection, malignancy), menstrual loss', 'Inadequate intake (poor diet)', 'Malabsorption (coeliac disease, gastrectomy)', 'Increased demand: infancy, adolescence, pregnancy']) +
 SH('Findings') +
 TB(['Test', 'Result'], [
  ['Haemoglobin, MCV, MCH, MCHC', 'Low'],
  ['RDW', 'High (anisocytosis)'],
  ['Peripheral smear', 'Microcytic hypochromic cells, pencil cells, target cells'],
  ['Serum iron and ferritin', 'Low'],
  ['TIBC', 'High; low transferrin saturation'],
  ['Bone marrow iron (Prussian blue)', 'Absent'],
 ]) +
 SH('Clinical features') + P('Pallor, fatigue, koilonychia, angular stomatitis, glossitis, pica, and rarely dysphagia (Plummer-Vinson syndrome with oesophageal web).')),

('HM', 'Megaloblastic anaemia: causes and the blood and marrow findings.',
 P('Megaloblastic anaemia', 'A macrocytic anaemia caused by impaired DNA synthesis due to deficiency of vitamin B12 or folate, which produces large abnormal precursors (megaloblasts) with asynchronous nuclear-cytoplasmic maturation.') +
 TB(['Deficiency', 'Causes'], [
  ['Vitamin B12', 'Pernicious anaemia (autoimmune gastritis, antibodies to intrinsic factor), gastrectomy, ileal disease or resection, fish tapeworm, strict vegetarian diet'],
  ['Folate', 'Poor diet, alcoholism, pregnancy, malabsorption, drugs (methotrexate, phenytoin, trimethoprim)'],
 ]) +
 SH('Findings') +
 UL(['Blood: macro-ovalocytes, hypersegmented neutrophils (more than 5 lobes), anisopoikilocytosis; pancytopenia in severe cases; high MCV.', 'Marrow: hypercellular with megaloblasts and giant metamyelocytes.', 'Ineffective erythropoiesis: raised LDH and indirect bilirubin.', 'Low serum B12 or folate.']) +
 SH('Neurology') + P('Vitamin B12 deficiency (not folate) causes subacute combined degeneration of the spinal cord (dorsal columns and lateral corticospinal tracts) and peripheral neuropathy.')),

('HM', 'Sickle cell disease: genetics, pathogenesis, clinical features and diagnosis.',
 P('Sickle cell disease', 'An autosomal recessive haemoglobinopathy caused by a point mutation in the beta-globin gene (chromosome 11), replacing glutamic acid with valine at position 6 to give haemoglobin S.') +
 SH('Pathogenesis') +
 UL(['On deoxygenation, HbS polymerises into rods that distort the red cell into a sickle shape.', 'Sickled cells are fragile (haemolysis) and rigid (vaso-occlusion).', 'Triggers: hypoxia, acidosis, dehydration. HbF protects against sickling.']) +
 SH('Clinical features') +
 UL(['Chronic haemolytic anaemia, jaundice, pigment gallstones', 'Vaso-occlusive crises: bone pain, dactylitis (hand-foot syndrome), acute chest syndrome, stroke', 'Autosplenectomy and susceptibility to encapsulated bacteria; Salmonella osteomyelitis', 'Aplastic crisis (parvovirus B19) and splenic sequestration crisis']) +
 SH('Diagnosis') + P('Peripheral smear with sickle cells and target cells, a sickling test (sodium metabisulphite), and haemoglobin electrophoresis or HPLC showing HbS.')),

('HM', 'Thalassaemia: classification, pathogenesis and findings in beta-thalassaemia major.',
 P('Thalassaemias', 'A group of inherited disorders with reduced synthesis of alpha or beta globin chains, causing microcytic hypochromic anaemia.') +
 TB(['Type', 'Genetics', 'Types and effect'], [
  ['Beta-thalassaemia', 'Mutations of the beta-globin gene (chromosome 11)', 'Minor (trait), intermedia, and major (homozygous, transfusion-dependent)'],
  ['Alpha-thalassaemia', 'Gene deletions on chromosome 16', 'One deleted: silent carrier; two: trait; three: HbH disease; four: hydrops fetalis (Hb Barts), fatal'],
 ]) +
 SH('Beta-thalassaemia major') +
 UL(['Presents after about 6 months when HbF falls. Severe anaemia, hepatosplenomegaly (extramedullary haematopoiesis).', 'Marrow expansion: crew-cut skull on X-ray, chipmunk facies, growth retardation.', 'Iron overload from transfusions and increased absorption: haemosiderosis, cardiac failure.', 'Smear: microcytic hypochromic cells, target cells, basophilic stippling, nucleated red cells.', 'Electrophoresis: markedly increased HbF, absent or reduced HbA; in the trait the HbA2 is raised.'])),
]))

# ------------------------------------------------------------------ 22 Leukaemias
TOPICS.append(('22', 'Leukaemias', 'HM', [
('HM', 'Classify leukaemias. Differentiate acute from chronic leukaemia.',
 P('Leukaemia', 'A malignant clonal proliferation of haematopoietic cells in the bone marrow, usually with spillage into the peripheral blood.') +
 TB(['', 'Lymphoid', 'Myeloid'], [
  ['Acute', 'Acute lymphoblastic leukaemia (ALL)', 'Acute myeloid leukaemia (AML)'],
  ['Chronic', 'Chronic lymphocytic leukaemia (CLL)', 'Chronic myeloid leukaemia (CML)'],
 ]) +
 TB(['Feature', 'Acute', 'Chronic'], [
  ['Cell type', 'Immature blasts (traditionally 20% or more in marrow)', 'Mature or maturing cells'],
  ['Onset', 'Abrupt, with marrow failure (anaemia, infection, bleeding)', 'Insidious, often found incidentally'],
  ['Course', 'Fatal in weeks to months if untreated', 'Months to years'],
  ['Age', 'ALL in children, AML in adults', 'Adults and the elderly'],
 ])),

('HM', 'Differentiate acute lymphoblastic leukaemia from acute myeloid leukaemia.',
 P('Acute leukaemias', 'Both show blasts in the marrow and blood, which crowd out normal haematopoiesis. They differ in lineage, age, morphology and cytochemistry.') +
 TB(['Feature', 'ALL', 'AML'], [
  ['Age', 'Children (peak 2 to 5 years)', 'Adults'],
  ['Blast morphology', 'Small to medium, scanty agranular cytoplasm, one or two nucleoli', 'Larger, more cytoplasm, granules, **Auer rods**'],
  ['Myeloperoxidase', 'Negative', 'Positive'],
  ['PAS', 'Block positivity', 'Negative or diffuse'],
  ['TdT', 'Positive (B or T lymphoblasts)', 'Negative'],
  ['Sites of spread', 'Lymph nodes, spleen, CNS and testis', 'Gums, skin, DIC in the promyelocytic type'],
  ['Cytogenetics', 'Hyperdiploidy, t(12;21), t(9;22) (poor)', 'APL: t(15;17) PML-RARA, treated with ATRA'],
 ]) +
 SH('Diagnosis') + P('Complete blood count and smear, bone marrow aspiration and biopsy, cytochemistry, immunophenotyping by flow cytometry, and cytogenetic and molecular studies.')),

('HM', 'Chronic myeloid leukaemia: genetics, clinical features, blood picture and phases.',
 P('Chronic myeloid leukaemia', 'A myeloproliferative neoplasm of the pluripotent stem cell with the **Philadelphia chromosome**, t(9;22), which produces the BCR-ABL1 fusion gene (a constitutively active tyrosine kinase).') +
 SH('Clinical features') + UL(['Middle age; insidious onset', 'Fatigue, weight loss, abdominal fullness from marked splenomegaly', 'Hypermetabolic symptoms (sweating)']) +
 SH('Laboratory') +
 UL(['Marked leucocytosis (often above 100,000 per microlitre) with the whole spectrum of granulocytic maturation and basophilia.', 'Low leucocyte (neutrophil) alkaline phosphatase score.', 'Marrow hypercellular with myeloid hyperplasia; BCR-ABL1 by PCR or FISH.']) +
 SH('Phases') + P('Chronic phase, accelerated phase, and blast crisis (myeloid in about two thirds, lymphoid in about one third). Treatment: imatinib and other tyrosine kinase inhibitors.')),

('HM', 'Chronic lymphocytic leukaemia: features and diagnosis.',
 P('Chronic lymphocytic leukaemia', 'A neoplasm of mature B lymphocytes, the commonest leukaemia of the elderly in the West. When confined to nodes and marrow it is called small lymphocytic lymphoma.') +
 UL(['Often found incidentally; lymphadenopathy and splenomegaly.', 'Peripheral lymphocytosis with small mature lymphocytes and characteristic **smudge cells**.', 'Immunophenotype: CD5, CD19, CD20 (weak) and CD23 positive.', 'Complications: hypogammaglobulinaemia and infections, autoimmune haemolytic anaemia and thrombocytopenia, transformation to large cell lymphoma (Richter syndrome).'])),
]))

# ------------------------------------------------------------------ 23 Bleeding disorders
TOPICS.append(('23', 'Bleeding and Coagulation Disorders', 'HM', [
('HM', 'Classify bleeding disorders. What screening tests are used and what do they show?',
 P('Bleeding disorders', 'Disorders of haemostasis in which the capacity to stop bleeding is impaired.') +
 UL(['**Vascular:** scurvy, Henoch-Schonlein purpura, hereditary haemorrhagic telangiectasia', '**Platelet:** thrombocytopenia (ITP, TTP, DIC, marrow failure), qualitative defects (aspirin, uraemia, Glanzmann thrombasthenia)', '**Coagulation factors:** haemophilia A and B, von Willebrand disease, vitamin K deficiency, liver disease, DIC']) +
 TB(['Disorder', 'Platelet count', 'Bleeding time', 'PT', 'aPTT'], [
  ['Haemophilia A or B', 'Normal', 'Normal', 'Normal', 'Prolonged'],
  ['von Willebrand disease', 'Normal', 'Prolonged', 'Normal', 'Prolonged or normal'],
  ['ITP', 'Low', 'Prolonged', 'Normal', 'Normal'],
  ['Vitamin K deficiency, warfarin', 'Normal', 'Normal', 'Prolonged', 'Prolonged or normal'],
  ['DIC', 'Low', 'Prolonged', 'Prolonged', 'Prolonged'],
 ]) +
 SH('If pushed') + P('Mucocutaneous bleeding (petechiae, epistaxis) suggests a platelet or von Willebrand problem; deep bleeding (haemarthrosis, muscle haematoma) suggests a coagulation factor deficiency.')),

('HM', 'Haemophilia A: genetics, pathology, clinical features and diagnosis.',
 P('Haemophilia A', 'An X-linked recessive deficiency of coagulation factor VIII, caused by mutations in the gene on Xq28. Haemophilia B (Christmas disease) is deficiency of factor IX.') +
 UL(['Affects males; carrier females; about one third of cases are new mutations.', 'Severity depends on the factor level: severe (below 1%) has spontaneous bleeding.', 'Clinical: haemarthrosis (knees, elbows) leading to arthropathy, muscle and soft tissue haematomas, prolonged bleeding after trauma or surgery, intracranial haemorrhage.']) +
 SH('Laboratory') + P('Prolonged aPTT that corrects on mixing; normal PT, bleeding time and platelet count; low factor VIII assay. von Willebrand factor level is normal, which separates it from von Willebrand disease.')),

('HM', 'Differentiate idiopathic thrombocytopenic purpura from thrombotic thrombocytopenic purpura.',
 P('Thrombocytopenic purpura', 'Both present with thrombocytopenia and purpura but have different mechanisms and treatment.') +
 TB(['Feature', 'ITP', 'TTP'], [
  ['Mechanism', 'Autoantibodies (IgG) to platelet glycoproteins IIb/IIIa cause splenic destruction', 'Deficiency of **ADAMTS13**; ultra-large von Willebrand multimers cause platelet microthrombi'],
  ['Setting', 'Acute post-viral in children; chronic in women aged 20 to 40', 'Adults; acquired autoantibody or hereditary'],
  ['Clinical', 'Isolated thrombocytopenia, petechiae, mucosal bleeding', 'Pentad: fever, thrombocytopenia, microangiopathic haemolytic anaemia, renal failure, neurological signs'],
  ['Smear', 'Large platelets; no schistocytes', 'Schistocytes (fragmented red cells)'],
  ['PT and aPTT', 'Normal', 'Normal (differs from DIC)'],
  ['Marrow', 'Normal or increased megakaryocytes', 'Increased megakaryocytes'],
  ['Treatment', 'Corticosteroids, IVIG, splenectomy', 'Plasma exchange'],
 ])),

('HM', 'What is DIC? Describe its causes, pathogenesis and laboratory findings.',
 P('Disseminated intravascular coagulation', 'An acquired syndrome of widespread activation of coagulation that produces fibrin microthrombi throughout the circulation, with consumption of platelets and clotting factors and secondary fibrinolysis, so that bleeding and thrombosis coexist.') +
 SH('Causes') +
 UL(['Sepsis (endotoxin, especially Gram-negative)', 'Obstetric: abruptio placentae, amniotic fluid embolism, retained dead fetus, pre-eclampsia', 'Malignancy: acute promyelocytic leukaemia, mucin-secreting adenocarcinomas', 'Trauma, burns, snake bite, transfusion reactions']) +
 SH('Pathogenesis') + P('Release of tissue factor or widespread endothelial injury activates the coagulation cascade. Microthrombi cause ischaemia and microangiopathic haemolysis; consumption of platelets and factors, with plasmin-mediated fibrinolysis, causes haemorrhage.') +
 SH('Laboratory findings') + UL(['Low platelets', 'Prolonged PT and aPTT', 'Low fibrinogen', 'Raised fibrin degradation products and D-dimer', 'Schistocytes on the smear']) +
 SH('Management') + P('Treat the underlying cause; supportive replacement of platelets, plasma and cryoprecipitate as needed.')),
]))
