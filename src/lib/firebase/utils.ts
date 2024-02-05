import { doc, setDoc, getDoc, DocumentReference } from "firebase/firestore";
import { auth, firestore } from "$lib/firebase/firebase";
import { signInWithPopup, GoogleAuthProvider } from "firebase/auth";

export async function initiateUser(docRef: DocumentReference, username: string) {
    await setDoc(
        docRef,
        {
            name: username,
            language: "en"
        },
        { merge: true }
    );
}

export async function signInWithAuth() {
    signInWithPopup(auth, new GoogleAuthProvider()).then(async ({ user }) => {
        let docRef = doc(firestore, "users", user.uid);

        if (!(await getDoc(docRef)).exists())
            await initiateUser(docRef, user.displayName as string);

        window.location.href = "/home";
    });
}
