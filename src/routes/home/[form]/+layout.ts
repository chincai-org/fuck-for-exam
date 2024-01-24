// @ts-ignore
import type { PageLoad } from "../[form]/$types";
import { recursiveFind } from "$lib/data/fetchData";
import { error } from "@sveltejs/kit";
import { auth, firestore } from "$lib/firebase/firebase";
import { doc, getDoc } from "firebase/firestore";
import type { Data } from "$lib/data/types";

export const load: PageLoad = async ({ params, url }: any) => {
    return new Promise(async (resolve, reject) => {
        const unsubscribe = auth.onAuthStateChanged(async user => {
            if (user) {
                // @ts-ignore
                const docRef = doc<Data>(firestore, "users", user.uid);
                // @ts-ignore
                const result = await getDoc<Data>(docRef);
                const data = result.data();

                console.log(user.uid);
                console.log(data);

                const routeList = [data.language].concat(Object.values(params));
                const buttons = recursiveFind(routeList);

                if (!buttons) {
                    error(404, {
                        message: "Not found"
                    });
                }

                resolve({
                    buttons
                });
            } else {
                error(403, {
                    message: "Unauthorized"
                });
            }

            // Unsubscribe the listener to avoid memory leaks
            unsubscribe();
        });
    });
};
