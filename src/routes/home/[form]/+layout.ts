import type { PageLoad } from "../[form]/$types";
import { recursiveFind } from "$lib/data/fetchData";
import { error } from "@sveltejs/kit";
import { docStore, userStore, User, SignedOut, Doc } from "sveltefire";
import { auth, firestore } from "$lib/firebase/firebase";

const user = userStore(auth);
const data = docStore(firestore, `users/${user?.uid}`);

export const load: any = (({ params, url }: any) => {
    url.href;
    let routeList = Object.values(params).unshift(data?.language)
    const buttons = recursiveFind(routeList);
    if (!buttons) {
        error(404, {
            message: "Not found"
        });
    }
    return {
        buttons
    };
}) satisfies PageLoad;
