import asyncio

from parsers.atptour_parser import ATPTourParser


async def main():
    parser = ATPTourParser()
    result = await parser.parse("https://www.atptour.com/en/players/jannik-sinner/s0ag/overview")

    print("\nTITLE:")
    print(result["title"])

    print("\nDOMAIN:")
    print(result["domain"])

    print("\nHTML TEXT PREVIEW:")
    print(result["html_text"][:3000])

    print("\nPARSED TEXT PREVIEW:")
    print(result["parsed_text"][:3000])

    print("\nLUNGHEZZE:")
    print(f'html_text: {len(result["html_text"])} caratteri')
    print(f'parsed_text: {len(result["parsed_text"])} caratteri')


if __name__ == "__main__":
    asyncio.run(main())