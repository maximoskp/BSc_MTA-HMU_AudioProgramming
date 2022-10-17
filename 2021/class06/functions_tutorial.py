# -*- coding: utf-8 -*-

# python functions:
# def FUNCTION_NAME( INPUT_ARGUMENTS, ... , ... )
# ____identation (εσοχή στο κείμενο, συνήθως 4 κενά)
# ____(στη συνάρτηση βρίσκεται ο κώδικας που ακολουθεί
# ____επιθυμητό πλήθος κενών).
# ____Η εμβέλεια των μεταβλητών που ορίζονται μέσα στη συνάρτηση,
# ____παραμένει μέσα στη συνάρτηση (cell 2). Αυτό το φαινόμενο
# ____καλείται "τοπική εμβέλεια". Οι μεταβλητές που ορίζονται εκτός
# ____συναρτήσεων, λέγεται ότι έχουν "καθολική εμβέλεια" (global 
# ____scope).

# κατασκευάζει τη συνάρτηση, δεν την τρέχει
def add_and_print( x , y ):
    z = x + y
    print('sum = ', z)
# ο ορισμός της συνάρτησης τελειώνει εδώ
print('out of the fuction')
m = 5 # είμαστε έξω από τη συνάρτηση
n = 6

# %% cell 0

# αν θέλουμε να τρέξουμε τη συνάρτηση
add_and_print( 3 , 4 )
add_and_print( 3 , 5 )
add_and_print( m , n )

# %% cell 1

import numpy as np

# για να φαίνεται πιο ευδιάκριτα το που τελειώνει η συνάρτηση
# μπορούμε να βάζουμε σχόλια στο τέλος ως εξής
def show_square_root( x ):
    print( 'square root of ' + str(x) + ' is ' + str(np.sqrt(x)) )
# show_square_root

show_square_root(10)

# %% cell 2

# θέλουμε όμως να προσθέσουμε τις τετραγωνικές ρίζες δύο αριθμών
# και να μας επιστρέφει το αποτέλεσμα
def sum_square_roots( x , y ):
    z = np.sqrt(x) + np.sqrt(y)
    if z >= 100:
        return z
    print('z < 100')
    return -1
# sum_square_roots

k = sum_square_roots( 5000 , 6000 )

# αν τρέξουμε το παρακάτω, θα βγάλει σφάλμα ότι δεν αναγνωρίζει
# τη μεταβλητή z, επειδή είναι ορισμένη μέσα στη συνάρτηση, άρα έχει
# "τοπική εμβέλεια" μέσα στη συνάρτηση.
# print(z)

# %% cell 3
# μία συνάρτηση μπορεί να επιστρέφει περισσότερες από 1 μεταβλητές

def compute_mean_and_max_and_min_of_array(x):
    x_mean = np.mean( x )
    x_max = np.max( x )
    x_min = np.min( x )
    return x_mean, x_max, x_min
# compute_mean_and_max_and_min_of_array

# t = np.array([ 1,2,3,4,5 ])
t = [ 1,2,3,4,5 ]

# αν η συνάρτηση κάνει return πολλές μεταβλητές κι εμείς
# αναθέσουμε ό,τι επιστρέφει σε μία μεταβλητή, τότε
# η μία μεταβλητή πουεπιτρέψει είναι ένα tuple
# r = compute_mean_and_max_and_min_of_array( t )


# ανάθεση της κάθε μεταβλητής επιστροφής, σε μία μεταβλητή εξόδου
r1, r2, r3 = compute_mean_and_max_and_min_of_array( t )

# για να αγνοήσουμε κάποιες γίνεται ως εξής
# πχ θέλουμε μόνο τη 2η
_, s2, _ = compute_mean_and_max_and_min_of_array( t )

# ΠΡΟΣΟΧΗ: ή βάζουμε μία έξοδο ή βάζουμε όσες εξόδους έχει το return
# με λιγότερες βγάζει σφάλμα - για να αγνοήσουμε κάποιες βάζουμε "_"
# r1, r2 = compute_mean_and_max_and_min_of_array( t )

# %% positional and keyword arguments

# τα ορίσματα (εισόδου) σε συναρτήσεις χωρίζονται σε θεσιακά και 
# λέξεις-κλειδιά

# %%

# παράδειγμα συνάρτησης με αποκλειστικά θεσιακά ορίσματα
def concatenate_and_print( s1, s2 ):
    s = s1 + s2
    print(s)
# concatenate_and_print

concatenate_and_print('xixi', 'lala')
# αλλάζοντας τη θέση των ορισμάτων, αλλάζει και το αποτέλεσμα
concatenate_and_print('lala', 'xixi')

# %% 

# παράδειγμα συνάρτησης με αποκλειστικά ορίσματα λέξεις-κλειδιά
def concatenate_and_print( s1='a', s2='b' ):
    s = s1 + s2
    print(s)
# concatenate_and_print

# μπορούμε να την καλέσουμε χωρίς τιμές στις λέξεις-κλειδιά
concatenate_and_print()
# μπορούμε να αλλάξουμε όποιο θέλουμε, ανεξάρτητα με τη
# σειρά που εμφανίζεται
concatenate_and_print(s2='lala')
# αν δεν ορίσουμε ποιο όρισμα λέξη-κλειδί θέλουμε να αλλάξει,
# τότε λειτουργούν ως θεσιακά
concatenate_and_print('lala')
concatenate_and_print('lala', s2='xixi')
# ή μπορούμε να ανακατέψουμε τη σειρά
concatenate_and_print(s2='lala', s1='xixi')


# ΠΡΟΣΟΧΗ: αν βάλουμε θεσιακό και λέξη-κλειδί σε λάθος σειρά, 
# δεν θα δουλέψει
# concatenate_and_print('lala', s1='xixi')

# %% συναρτήσεις με θεσιακά και λέξεις-κλειδιά ορίσματα

def concatenate_and_print( s1, s2='b', s3='c'  ):
    s = s1 + s2 + s3
    print(s)
# concatenate_and_print

# ΠΡΟΣΟΧΗ: αν η συνάρτηση έχει θεσιακά και λέξεις-κλειδιά,
# τα θεσιακά πρέπει να δίνονται πρώτα. Δηλαδή, το παρακάτω δεν 
# θα δουλέψει:
'''
def concatenate_and_print( s1='a', s2, s3='c'  ):
    s = s1 + s2 + s3
    print(s)
# concatenate_and_print
'''

concatenate_and_print('xix')
concatenate_and_print('xix', s3='lala')

# ΔΕΝ θα δουλέψει
# ΚΑΙ στον ορισμό αλλά ΚΑΙ στην κλήση της συνάρτησης,
# τα θεσιακά μπαίνουν πρώτα
# concatenate_and_print(s2='lala', 'xix')













