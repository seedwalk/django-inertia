
import { Link, router } from "@inertiajs/react";
import { useState } from "react";

export default function Villains({ villains, pagination, filters }) {
  const [selectedUniverse, setSelectedUniverse] = useState(filters.universe || "");

  const handleUniverseFilter = (universe) => {
    setSelectedUniverse(universe);
    router.get("/villains", { universe, page: 1 }, { preserveState: true });
  };

  const goToPage = (page) => {
    router.get(
      "/villains",
      { page, universe: selectedUniverse },
      { preserveState: true }
    );
  };

  return (
    <div className="min-h-screen bg-slate-950">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-5xl font-bold text-red-500 mb-4">
            Villains Gallery
          </h1>
          <p className="text-xl text-slate-300">
            Los villanos más temibles del universo
          </p>
          <div className="mt-2 text-slate-400">
            Total de villanos: <span className="text-red-400 font-semibold">{pagination?.total || 0}</span>
          </div>
        </div>

        {/* Navigation */}
        <div className="mb-8 flex justify-center gap-3">
          <Link
            href="/"
            className="px-5 py-2 rounded-lg font-semibold transition-all bg-slate-800 text-slate-300 hover:bg-slate-700"
          >
            🦸 Ver Héroes
          </Link>
          <Link
            href="/villains"
            className="px-5 py-2 rounded-lg font-semibold transition-all bg-red-600 text-white shadow-lg"
          >
            🦹 Ver Villanos
          </Link>
        </div>

        {/* Filters */}
        <div className="mb-8 flex justify-center gap-3">
          <button
            onClick={() => handleUniverseFilter("")}
            className={`px-5 py-2 rounded-lg font-semibold transition-all ${
              selectedUniverse === ""
                ? "bg-red-600 text-white shadow-lg"
                : "bg-slate-800 text-slate-300 hover:bg-slate-700"
            }`}
          >
            Todos
          </button>
          <button
            onClick={() => handleUniverseFilter("MARVEL")}
            className={`px-5 py-2 rounded-lg font-semibold transition-all ${
              selectedUniverse === "MARVEL"
                ? "bg-red-700 text-white shadow-lg"
                : "bg-slate-800 text-slate-300 hover:bg-slate-700"
            }`}
          >
            Marvel
          </button>
          <button
            onClick={() => handleUniverseFilter("DC")}
            className={`px-5 py-2 rounded-lg font-semibold transition-all ${
              selectedUniverse === "DC"
                ? "bg-purple-600 text-white shadow-lg"
                : "bg-slate-800 text-slate-300 hover:bg-slate-700"
            }`}
          >
            DC Comics
          </button>
        </div>

        {/* Villains Grid */}
        {villains && villains.length > 0 ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {villains.map((villain) => (
              <div
                key={villain.id}
                className="bg-slate-800 rounded-lg overflow-hidden border border-red-900 hover:border-red-600 transition-all duration-300 hover:shadow-xl hover:shadow-red-900/50"
              >
                {/* Villain Image */}
                <div className="relative h-64 bg-slate-900">
                  {villain.profileImage ? (
                    <img
                      src={villain.profileImage}
                      alt={villain.name}
                      className="w-full h-full object-cover"
                    />
                  ) : (
                    <div className="w-full h-full flex items-center justify-center bg-slate-800">
                      <div className="text-6xl text-slate-600">😈</div>
                    </div>
                  )}
                  {/* Power Level Badge */}
                  <div className="absolute top-3 right-3 bg-red-600 px-3 py-1 rounded-full">
                    <span className="text-white font-bold text-sm">
                      ⚡ {villain.powerLevel}
                    </span>
                  </div>
                </div>

                {/* Villain Info */}
                <div className="p-5">
                  <h3 className="text-2xl font-bold text-red-400 mb-1">
                    {villain.name}
                  </h3>
                  {villain.realName && (
                    <p className="text-slate-400 text-sm mb-3">
                      {villain.realName}
                    </p>
                  )}

                  {/* Universe Badge */}
                  <div className="mb-3">
                    <span className="inline-block bg-slate-700 text-slate-200 px-3 py-1 rounded-full text-xs font-semibold">
                      {villain.universe}
                    </span>
                  </div>

                  {/* Powers */}
                  {villain.powers && villain.powers.length > 0 && (
                    <div className="mb-4">
                      <h4 className="text-xs font-semibold text-slate-400 mb-2">
                        PODERES:
                      </h4>
                      <div className="flex flex-wrap gap-1">
                        {villain.powers.slice(0, 3).map((power, idx) => (
                          <span
                            key={idx}
                            className="inline-block bg-red-900/30 text-red-300 px-2 py-1 rounded text-xs border border-red-800"
                          >
                            {power}
                          </span>
                        ))}
                        {villain.powers.length > 3 && (
                          <span className="inline-block bg-red-900/30 text-red-300 px-2 py-1 rounded text-xs border border-red-800">
                            +{villain.powers.length - 3} más
                          </span>
                        )}
                      </div>
                    </div>
                  )}

                  {/* Action Link */}
                  <Link 
                    href={`/${villain.id}`}
                    className="block w-full text-center px-4 py-2 rounded-md bg-red-600 hover:bg-red-500 text-white transition-colors font-medium"
                  >
                    Ver Detalles
                  </Link>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="text-center py-20">
            <div className="text-6xl mb-4">🦹</div>
            <p className="text-2xl text-slate-300 mb-4">
              No hay villanos disponibles
            </p>
            <p className="text-slate-400">
              Ejecuta el comando seed para agregar villanos a la base de datos
            </p>
          </div>
        )}

        {/* Pagination */}
        {pagination && pagination.lastPage > 1 && (
          <div className="mt-12 flex justify-center items-center gap-2">
            {/* Previous Button */}
            <button
              onClick={() => goToPage(pagination.currentPage - 1)}
              disabled={!pagination.hasPreviousPage}
              className={`px-4 py-2 rounded-lg font-semibold transition-all ${
                pagination.hasPreviousPage
                  ? "bg-slate-800 text-slate-300 hover:bg-slate-700"
                  : "bg-slate-900 text-slate-600 cursor-not-allowed"
              }`}
            >
              ← Anterior
            </button>

            {/* Page Numbers */}
            <div className="flex gap-2">
              {[...Array(pagination.lastPage)].map((_, i) => {
                const pageNum = i + 1;
                // Mostrar solo páginas cercanas
                if (
                  pageNum === 1 ||
                  pageNum === pagination.lastPage ||
                  (pageNum >= pagination.currentPage - 1 &&
                    pageNum <= pagination.currentPage + 1)
                ) {
                  return (
                    <button
                      key={pageNum}
                      onClick={() => goToPage(pageNum)}
                      className={`px-4 py-2 rounded-lg font-semibold transition-all ${
                        pageNum === pagination.currentPage
                          ? "bg-red-600 text-white"
                          : "bg-slate-800 text-slate-300 hover:bg-slate-700"
                      }`}
                    >
                      {pageNum}
                    </button>
                  );
                } else if (
                  pageNum === pagination.currentPage - 2 ||
                  pageNum === pagination.currentPage + 2
                ) {
                  return (
                    <span key={pageNum} className="px-2 py-2 text-slate-500">
                      ...
                    </span>
                  );
                }
                return null;
              })}
            </div>

            {/* Next Button */}
            <button
              onClick={() => goToPage(pagination.currentPage + 1)}
              disabled={!pagination.hasNextPage}
              className={`px-4 py-2 rounded-lg font-semibold transition-all ${
                pagination.hasNextPage
                  ? "bg-slate-800 text-slate-300 hover:bg-slate-700"
                  : "bg-slate-900 text-slate-600 cursor-not-allowed"
              }`}
            >
              Siguiente →
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

