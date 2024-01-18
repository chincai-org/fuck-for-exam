<script lang="ts">
    import { SignedIn, SignedOut, Doc, Collection } from "sveltefire";
    import { signInWithPopup, GoogleAuthProvider } from "firebase/auth";
    import { auth } from "$lib/firebase/firebase";
</script>

<button
    on:click={() =>
        signInWithPopup(auth, new GoogleAuthProvider()).then(() => {
            window.location.href = "/home";
        })}
>
    Sign In
</button>
