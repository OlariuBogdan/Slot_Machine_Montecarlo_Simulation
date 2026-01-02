import random
import setari as s
import time

# --- COPIEM LOGICA DE BUSINESS DIN JOC (Fără Grafică) ---

def get_simboluri_rola(id_rola):
    """ Alege 3 simboluri random de pe banda rolei specificate. """
    banda = s.BENZI_ROLE[id_rola]
    lungime = len(banda)
    index_stop = random.randint(0, lungime - 1)
    
    # Simulare fereastră 3 poziții (Sus, Mijloc, Jos)
    index_sus = (index_stop - 1) % lungime
    index_mijloc = index_stop
    index_jos = (index_stop + 1) % lungime
    
    return [banda[index_sus], banda[index_mijloc], banda[index_jos]]

def calculeaza_castig_linie(simboluri, miza_pe_linie):
    """ Logica exactă de verificare a liniei (inclusiv WILD). """
    primul_simbol = simboluri[0]
    
    # Scatter nu plătește pe linie
    if primul_simbol == s.SCATTER:
        return 0
    
    # Gestionare WILD la început
    if primul_simbol == s.WILD:
        simbol_non_wild_gasit = False
        for simbol_non_wild in simboluri[1:]:
            if simbol_non_wild != s.WILD and simbol_non_wild != s.SCATTER:
                primul_simbol = simbol_non_wild
                simbol_non_wild_gasit = True
                break
        # Dacă sunt doar Wild-uri, plătim ca pentru Șeptari
        if not simbol_non_wild_gasit:
            return s.TABEL_PLATA[s.SAPTE][5] * miza_pe_linie

    # Numărăm simbolurile consecutive
    numar_consecutive = 0
    for simbol in simboluri:
        if simbol == primul_simbol or simbol == s.WILD:
            numar_consecutive += 1
        else:
            break
    
    # Verificăm tabelul de plată
    if numar_consecutive >= 3:
        if primul_simbol in s.TABEL_PLATA:
            return s.TABEL_PLATA[primul_simbol][numar_consecutive] * miza_pe_linie
            
    return 0

def verificare_scatter(matrice, miza_totala):
    count = 0
    for rand in matrice:
        for simbol in rand:
            if simbol == s.SCATTER:
                count += 1
    if count in s.PLATA_SCATTER:
        return s.PLATA_SCATTER[count] * miza_totala
    return 0

# --- MOTE CARLO ENGINE ---

def ruleaza_simulare(nr_rotiri=1000000):
    print(f"--- Începe Simularea Monte Carlo ({nr_rotiri} rotiri) ---")
    start_time = time.time()
    
    miza_pe_linie = 1.0
    nr_linii = len(s.LINII_PLATA)
    miza_totala_per_spin = miza_pe_linie * nr_linii
    
    total_pariat = 0
    total_castigat = 0
    nr_castiguri = 0 # Pentru Hit Frequency
    cel_mai_mare_castig = 0
    
    for i in range(nr_rotiri):
        # 1. Pariază
        total_pariat += miza_totala_per_spin
        
        # 2. Generează Matricea (RNG)
        # Transpunem logica: 5 role a câte 3 simboluri
        coloane = [get_simboluri_rola(i) for i in range(5)]
        # Transformăm în matrice rânduri (3x5)
        matrice = [list(rand) for rand in zip(*coloane)]
        
        castig_spin = 0
        
        # 3. Verifică Liniile
        for linie_indecsi in s.LINII_PLATA.values():
            simboluri_linie = []
            for id_col, id_rand in enumerate(linie_indecsi):
                simboluri_linie.append(matrice[id_rand][id_col])
            
            castig_spin += calculeaza_castig_linie(simboluri_linie, miza_pe_linie)
            
        # 4. Verifică Scatter
        castig_spin += verificare_scatter(matrice, miza_totala_per_spin)
        
        # 5. Statistici
        total_castigat += castig_spin
        if castig_spin > 0:
            nr_castiguri += 1
            if castig_spin > cel_mai_mare_castig:
                cel_mai_mare_castig = castig_spin
                
        # Progres (la fiecare 10%)
        if i % (nr_rotiri // 10) == 0 and i > 0:
            print(f"Progres: {i} rotiri... RTP momentan: {(total_castigat/total_pariat)*100:.2f}%")

    end_time = time.time()
    durata = end_time - start_time
    
    # --- RAPORT FINAL ---
    rtp_final = (total_castigat / total_pariat) * 100
    hit_frequency = (nr_castiguri / nr_rotiri) * 100
    
    print("\n" + "="*40)
    print(f"REZULTATE SIMULARE ({nr_rotiri} rotiri)")
    print("="*40)
    print(f"Timp execuție: {durata:.2f} secunde")
    print(f"Total Pariat:  {total_pariat:,.0f} RON")
    print(f"Total Returnat:{total_castigat:,.0f} RON")
    print("-" * 20)
    print(f"RTP CALCULAT:  {rtp_final:.4f}%")
    print(f"HIT FREQUENCY: {hit_frequency:.2f}% (Câștigi la fiecare {100/hit_frequency:.1f} rotiri)")
    print(f"MAX WIN:       {cel_mai_mare_castig} RON")
    print("="*40)

if __name__ == "__main__":
    ruleaza_simulare(1_000_000)