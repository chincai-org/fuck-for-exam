import type { PageLoad } from "./$types";
import { recursiveFind } from "$lib/data/fetchData";
import { error } from "@sveltejs/kit";

export const load: any = (({ params, url }: any) => {
    url.href;
    const buttons = recursiveFind(Object.values(params));

    if (!buttons) {
        error(404, {
            message: "Not found"
        });
    }

    return {
        buttons
    };
}) satisfies PageLoad;
