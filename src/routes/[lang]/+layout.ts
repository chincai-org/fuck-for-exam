import type { PageLoad } from "./$types";
import { findData, recursiveFind } from "$lib/data/fetchData";

export const load: any = (({ params }: any) => {
    console.log(window.location.href);
    console.log(params.lang);
    console.log(params.form);
    console.log(params.subject);
    console.log(params.bab);

    const rawRoutes: string = window.location.href.replace(/https?:\/\/[^\/]+\//, "");
    const routeList: Array<string> = rawRoutes.split("/");
    console.log(routeList);
    const buttons = recursiveFind(routeList);

    console.log(buttons);

    console.log(`/${params.lang}`);
    return {
        buttons: buttons,
        test: 0
    };
}) satisfies PageLoad;
