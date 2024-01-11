import type { PageLoad } from "./$types";
import { findData, recursiveFind } from "$lib/data/fetchData";
import { error } from '@sveltejs/kit'

export const load: any = (({ params }: any) => {
    console.log(window.location.href);
    console.log(params);

    const rawRoutes: string = window.location.href.replace(/https?:\/\/[^\/]+\//, "");
    const routeList: Array<string> = rawRoutes.split("/");
    console.log(routeList);
    const buttons = recursiveFind(routeList);

    if (!buttons) {
        error(404, {
			message: 'Not found'
		});  
    }

    console.log(buttons);

    console.log(`/${params.language}`);

    return {
        buttons: buttons,
    };
}) satisfies PageLoad;