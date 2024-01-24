<script lang="ts">
    import {
        signInWithPopup,
        GoogleAuthProvider,
        createUserWithEmailAndPassword
    } from "firebase/auth";
    import { doc, setDoc, getDoc } from "firebase/firestore";
    import { auth, firestore } from "$lib/firebase/firebase";
    import { goto } from "$app/navigation";

    let name: string;
    let email: string;
    let password: string;
    let cpassword: string;

    let warning: string = "";

    async function signUp() {
        if (name == "") {
            warning = "Please fill in the name";
            return;
        } else if (password != cpassword) {
            warning = "Password does not match";
            return;
        }

        createUserWithEmailAndPassword(auth, email, password)
            .then(async ({ user }) => {
                let docRef = doc(firestore, "users", user.uid);
                if (!(await getDoc(docRef)).exists())
                    await setDoc(docRef, {
                        name: name,
                        language: "en"
                    });
                window.location.href = "/home";
            })
            .catch(reason => {
                console.log(reason);
                window.location.href = "/";
            });
    }

    async function signInWithAuth() {
        signInWithPopup(auth, new GoogleAuthProvider()).then(async ({ user }) => {
            let docRef = doc(firestore, "users", user.uid);

            if (!(await getDoc(docRef)).exists())
                await setDoc(
                    docRef,
                    {
                        name: user.displayName,
                        language: "en"
                    },
                    { merge: true }
                );

            window.location.href = "/home";
        });
    }
</script>

<p>{warning}</p>

<input type="text" bind:value={email} placeholder="Enter email" required />
<input type="text" bind:value={name} placeholder="Full name" required />
<input type="password" bind:value={password} placeholder="Enter password" required />
<input type="password" bind:value={cpassword} placeholder="Confirm password" required />
<button on:click={signUp}>Sign up</button>

<button on:click={signInWithAuth}>Sign up with Google</button>
